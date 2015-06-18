# -*- coding: utf-8 -*-
# __author__ = 'chenzhi'

import os
import jieba
import jieba.analyse
from gensim import corpora, models, similarities


STOP_WORDS_PATH = "/home/chenzhi/Documents/SogouC.reduced/stop_words"
with open(STOP_WORDS_PATH, "r") as f:
    STOP_WORDS = f.readlines()
STOP_WORDS = [word.decode("utf-8").replace("\n", "") for word in STOP_WORDS]


def test_encoding():
    path = "/home/chenzhi/Documents/SogouC.reduced/Reduced/C000008/10.txt"
    with open(path, "r") as f:
        content = f.readlines()

    for line in content:
        print line.decode("GB2312").encode("utf-8")


def text_to_vector(f):
    if isinstance(f, str):
        f = open(f, "r")
    text = f.readlines()
    f.close()
    text = [line.decode("GB2312").encode("utf-8") for line in text]
    text = "".join(text).replace("\r\n", "").replace("\t", "")
    seg_list = jieba.cut(text)
    seg_list = [seg for seg in seg_list if seg not in STOP_WORDS]
    return seg_list


def text_to_vector(text_path):
    with open(text_path, "r") as f:
        text = f.readlines()
    try:
        text = [line.decode("GB2312").encode("utf-8") for line in text]
    except Exception as e:
        text = [line.decode("GB18030").encode("utf-8") for line in text]
    text = "".join(text).replace("\r\n", "").replace("\t", "")
    seg_list = jieba.cut(text)
    seg_list = [seg for seg in seg_list if seg not in STOP_WORDS and seg != u"" and seg != u"\n"]
    return seg_list


def directory_to_vectors(path):
    vectors = []
    for file in read_directory(path):
        vectors.append(text_to_vector(file))
    return vectors


def read_directory(root_dir):
    all_files = []
    for root, sub_dirs, files in os.walk(root_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files


def save_dictionary_and_corpus():
    vectors = directory_to_vectors("/home/chenzhi/Documents/SogouC.reduced/Sample/Sample")
    dictionary = corpora.Dictionary(vectors)
    # vd = dict([(v,k) for (k,v) in dictionary.token2id.items()])
    dictionary.save_as_text('/home/chenzhi/Documents/SogouC.reduced/Sample/dictionary.txt')
    print dictionary

    corpus = [dictionary.doc2bow(vector) for vector in vectors]
    corpora.MmCorpus.serialize('/home/chenzhi/Documents/SogouC.reduced/Sample/corpus.mm', corpus)
    print corpus

    # print dictionary.token2id



def main():
    """
    before running main(), please run save_dictionary_and_corpus(), it will prepare data required by main()
    :return:
    """
    id2word = corpora.Dictionary.load_from_text('/home/chenzhi/Documents/SogouC.reduced/Sample/dictionary.txt')
    print id2word
    mm = corpora.MmCorpus('/home/chenzhi/Documents/SogouC.reduced/Sample/corpus.mm')
    print mm

    lsi = models.lsimodel.LsiModel(corpus=mm, id2word=id2word, num_topics=10)

    topics =  lsi.print_topics(10)
    print topics

if __name__ == "__main__":
    # id2word = corpora.Dictionary.load_from_text('/home/chenzhi/Documents/SogouC.reduced/Sample/dictionary.txt')
    # print(id2word.token2id)
    # save_dictionary_and_corpus()
    main()