from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt, mpld3
stopwords = set(STOPWORDS)


class WordClouds(object):
    def show_wordcloud(self, data, title = None):
        wordcloud = WordCloud(
            background_color='black',
            max_words=200,
            max_font_size=40,
            scale=3,
            random_state=1 # chosen at random by flipping a coin; it was heads
        ).generate_from_frequencies(data)

        fig = plt.figure(1, figsize=(12, 12))
        plt.axis('off')
        if title:
            fig.suptitle(title, fontsize=20)
            fig.subplots_adjust(top=2.3)

        plt.imshow(wordcloud)
        output = mpld3.fig_to_html(fig)
        return output
