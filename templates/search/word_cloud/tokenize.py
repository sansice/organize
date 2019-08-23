import re
import sys
from collections import defaultdict
from operator import itemgetter

from search.utils import const

import numpy as np


class Tokenize(object):
    def __init__(self, data):
        self.input_string = data
        self.regexp = r"\w[\w']+"
        self.include_numbers = True
        self.min_word_length = 2
        self.normalize_plurals = True

    def get_unique_words(self):
        counts = dict()
        words = self.input_string.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts

    @staticmethod
    def get_stop_words():
        stopword_file = const.stopwords_file
        return set(map(str.strip, open(stopword_file).readlines()))

    def process_text(self):
        """Splits a long text into words, eliminates the stopwords.

        Parameters
        ----------

        Returns
        -------
        words : dict (string, int)
            Word tokens with associated frequency.

        ..versionchanged:: 1.2.2
            Changed return type from list of tuples to dict.

        Notes
        -----
        There are better ways to do word tokenization, but I don't want to
        include all those things.
        """

        stopwords = set([i.lower() for i in self.get_stop_words()])

        flags = (re.UNICODE if sys.version < '3' and type(self.input_string) is np.unicode  # noqa: F821
                 else 0)
        regexp = self.regexp if self.regexp is not None else r"\w[\w']+"

        words = re.findall(regexp, self.input_string, flags)
        # remove stopwords
        words = [word for word in words if word.lower() not in stopwords]
        # remove 's
        words = [word[:-2] if word.lower().endswith("'s") else word
                 for word in words]
        # remove numbers
        if not self.include_numbers:
            words = [word for word in words if not word.isdigit()]
        # remove short words
        if self.min_word_length:
            words = [word for word in words if len(word) >= self.min_word_length]

        word_counts, _ = self.process_tokens(words, self.normalize_plurals)
        return self.convert_data_json(word_counts)

    @staticmethod
    def convert_data_json(word_counts):
        return_list = []
        for word in word_counts:
            text_val = {'text': word, 'value': word_counts[word]}
            return_list.append(text_val)
        return return_list

    @staticmethod
    def process_tokens(words, normalize_plurals=True):
        """Normalize cases and remove plurals.

        Each word is represented by the most common case.
        If a word appears with an "s" on the end and without an "s" on the end,
        the version with "s" is assumed to be a plural and merged with the
        version without "s" (except if the word ends with "ss").

        Parameters
        ----------
        words : iterable of strings
            Words to count.

        normalize_plurals : bool, default=True
            Whether to try and detect plurals and remove trailing "s".

        Returns
        -------
        counts : dict from string to int
            Counts for each unique word, with cases represented by the most common
            case, and plurals removed.

        standard_forms : dict from string to string
            For each lower-case word the standard capitalization.
        """
        # words can be either a list of unigrams or bigrams
        # d is a dict of dicts.
        # Keys of d are word.lower(). Values are dicts
        # counting frequency of each capitalization
        d = defaultdict(dict)
        merged_plurals = {}
        for word in words:
            word_lower = word.lower()
            # get dict of cases for word_lower
            case_dict = d[word_lower]
            # increase this case
            case_dict[word] = case_dict.get(word, 0) + 1
        if normalize_plurals:
            # merge plurals into the singular count (simple cases only)
            for key in list(d.keys()):
                if key.endswith('s') and not key.endswith("ss"):
                    key_singular = key[:-1]
                    if key_singular in d:
                        dict_plural = d[key]
                        dict_singular = d[key_singular]
                        for word, count in dict_plural.items():
                            singular = word[:-1]
                            dict_singular[singular] = (dict_singular.get(singular, 0) + count)
                        merged_plurals[key] = key_singular
                        del d[key]
        fused_cases = {}
        standard_cases = {}
        item1 = itemgetter(1)
        for word_lower, case_dict in d.items():
            # Get the most popular case.
            first = max(case_dict.items(), key=item1)[0]
            fused_cases[first] = sum(case_dict.values())
            standard_cases[word_lower] = first
        if normalize_plurals:
            # add plurals to fused cases:
            for plural, singular in merged_plurals.items():
                standard_cases[plural] = standard_cases[singular.lower()]
        return fused_cases, standard_cases
