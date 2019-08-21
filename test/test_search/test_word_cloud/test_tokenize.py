import os
import unittest
from general import utils
from search.word_cloud.tokenize import Tokenize


class TestTokenize(unittest.TestCase):

    def setUp(self):
        input_text_file = r"D:\sans\OneDrive - HCL Technologies Ltd\work\HCL\projects\organize\test\test_search\test_word_cloud\sample_text1"
        input_text = utils.file_to_string(input_text_file)
        self.wc = Tokenize(input_text)

    def tearDown(self) -> None:
        pass

    # def test_convert_data_json(self):
    #     processed_text = self.wc.process_text()
    #     self.wc.convert_data_json(processed_text)

    def test_process_text(self):
        processed_text = self.wc.process_text()
        print(processed_text)

    def test_get_stop_words(self):
        stopwords = self.wc.get_stop_words()
        print(stopwords)


if __name__ == '__main__':
    unittest.main()
