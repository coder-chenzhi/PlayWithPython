# -*- coding: utf-8 -*-
# __author__ = 'chenzhi'

from __future__ import unicode_literals
import jieba
import jieba.analyse

def read_data(path):
    with open(path) as f:
        content = f.readlines()
    # remove all timestamp
    content = [line if not line.startswith("2015".decode("utf-8").encode("utf-8")) else "" for line in content]
    content = [line.decode("utf-8") for line in content]
    return content

def main():
    topK = 30
    withWeight = True
    lines = read_data("G:\Personal Affair\DanielLovesLily\ChatLog\Lily(2392781997)-2015.5.10.txt")
    all_line = u" ".join(lines)
    jieba.analyse.set_stop_words("G:\Personal Affair\DanielLovesLily\ChatLog\stopwords2")
    tags = jieba.analyse.extract_tags(all_line, topK=topK, withWeight=withWeight)
    for tag in tags:
        print tag[0].encode("utf-8"), tag[1]

if __name__ == "__main__":
    main()

"""
The complete version.

# -*- coding: utf-8 -*-
# __author__ = 'chenzhi'

from __future__ import unicode_literals
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def read_data(path):
    with open(path) as f:
        content = f.readlines()
    # remove all timestamp
    content = [line if not line.startswith("2015".decode("utf-8").encode("utf-8")) else "" for line in content]
    content = [line.decode("utf-8") for line in content]
    return content

def main():
    topK = 50
    withWeight = True
    lines = read_data("/home/ubuntu/Documents/Lily(2392781997)-2015.5.10.txt")
    all_line = u" ".join(lines)
    jieba.analyse.set_stop_words("/home/ubuntu/Documents/stopwords")
    tags = jieba.analyse.extract_tags(all_line, topK=topK, withWeight=withWeight)
    for tag in tags:
        print tag[0].encode("utf-8"), tag[1]

    # generate word cloud
    wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/SHISHANG.ttf', background_color="white").generate_from_frequencies(tags)
    # Open a plot of the generated image.
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
"""