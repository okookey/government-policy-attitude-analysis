from typing import Dict
import wordcloud as wc
import matplotlib.pyplot as plt


class MakeWordCloud:
    def cloud_set(self, input_dict: Dict[str, int]):
        word_count_img = wc.WordCloud(
            width=1920,
            height=1080,
            font_path='./SimHei.ttf',
            background_color="black",
            max_font_size=300,
            random_state=5
        ).fit_words(input_dict)

        plt.figure()
        plt.imshow(word_count_img)
        plt.axis("off")
        plt.show()
