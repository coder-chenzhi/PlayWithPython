# -*- coding: utf-8 -*-
# __author__ = 'chenzhi'

import os
import jieba
import jieba.analyse
from gensim import corpora, models, similarities


STOP_WORDS_PATH = "G:\\Temp\\SogouC.reduced\\stop_words_sogou_reduced"
STOP_WORDS_MAP = {}
with open(STOP_WORDS_PATH, "r") as f:
    STOP_WORDS = f.readlines()
for word in STOP_WORDS:
    STOP_WORDS_MAP[word.decode("utf-8").replace("\n", "")] = 0


def test_encoding():
    path = "/home/chenzhi/Documents/SogouC.reduced/Reduced/C000008/10.txt"
    with open(path, "r") as f:
        content = f.readlines()

    for line in content:
        print line.decode("GB2312").encode("utf-8")


def try_to_decode(path):
    for file in read_directory(path):
        with open(file, "r") as f:
            text = f.readlines()
        try:
            text = [line.decode("GB2312").encode("utf-8") for line in text]
        except Exception as e:
            try:
                text = [line.decode("GB18030").encode("utf-8") for line in text]
            except Exception as e:
                print file


def text_to_vector(text_path):
    with open(text_path, "r") as f:
        text = f.readlines()
    try:
        text = [line.decode("GB2312").encode("utf-8") for line in text]
    except Exception as e:
        text = [line.decode("GB18030").encode("utf-8") for line in text]
    text = "".join(text).replace("\r\n", "").replace("\t", "")
    seg_list = jieba.cut(text)
    seg_list = [seg for seg in seg_list if seg not in STOP_WORDS_MAP and seg != u"" and seg != "\x00" and seg != u"\n"]
    return seg_list


def directory_to_vectors(path):
    """
    read all the documents in specific path, each document is a article, and return
    term-document matrix
    :param path: where the data locate
    :return: term-document matrix
    """
    texts = []
    for i, file in enumerate(read_directory(path)):
        texts.append(text_to_vector(file))
        if i % 10 == 0:
            print "\tHave parsed %d files." % i

    # remove words only appear once
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]
    return texts


def read_directory(root_dir):
    all_files = []
    for root, sub_dirs, files in os.walk(root_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    sorted(all_files)

    def save_id_to_filename(path, allfiles):
        f = open(path, 'w')
        for id, filename in enumerate(allfiles):
            f.write(str(id) + " " + filename + "\n")
        f.close()

    save_id_to_filename("G:\Temp\SogouC.reduced\Reduced\\id_to_filename", all_files)
    return all_files


def save_dictionary_and_corpus(data_path, save_path):
    """
    save corpus and dictionary svd needed, we can readily get the term-document matrix by reading corpus and
    dictionary, which can save much time by avoiding reread the primary files
    :param data_path: where the primary data locate
    :param save_path:where to save the corpus and dictionary
    :return:
    """
    print "Parse text to vector..."
    vectors = directory_to_vectors(data_path)
    print "Build dictionary from vector..."
    dictionary = corpora.Dictionary(vectors)
    # vd = dict([(v,k) for (k,v) in dictionary.token2id.items()])
    print "Save dictionary to disk..."
    dictionary.save_as_text(save_path + 'dictionary.txt')
    # print dictionary
    print "Build corpus from dictionary..."
    corpus = [dictionary.doc2bow(vector) for vector in vectors]
    print "Save corpus to disk..."
    corpora.MmCorpus.serialize(save_path + 'corpus.mm', corpus)
    # print corpus

    # print dictionary.token2id


def main(dictionary_path, corpus_path):
    """
    before running main(), please run save_dictionary_and_corpus(), it will prepare data required by main()
    :return:
    """
    id2word = corpora.Dictionary.load_from_text(dictionary_path)
    # print id2word
    corpus = corpora.MmCorpus(corpus_path)
    # print corpus
    # calculate TF-IDF
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    lsi = models.lsimodel.LsiModel(corpus=corpus_tfidf, id2word=id2word, num_topics=9)

    # official API to print topics
    # topics = lsi.print_topics(num_topics=9, num_words=20)
    # print topics

    def print_topic(n):
        for i in range(n):
            # print ",".join([str(tu[0]) + "*" + tu[1].encode("utf-8") for tu in lsi.show_topic(i, topn=20)])
            print ",".join(tu[1].encode("utf-8") for tu in lsi.show_topic(i, topn=20))

    print_topic(10)

    # LDA Model
    # lda = models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000, passes=1)
    # lda.print_topics(20)

if __name__ == "__main__":
    # id2word = corpora.Dictionary.load_from_text('/home/chenzhi/Documents/SogouC.reduced/Sample/dictionary.txt')
    # print(id2word.token2id)
    # try_to_decode("G:\\Temp\\SogouC.reduced\\Reduced\\data\\")
    # save_dictionary_and_corpus("G:\\Temp\\SogouC.reduced\\Reduced\\data\\", "G:\\Temp\\SogouC.reduced\\Reduced\\")
    main("G:\\Temp\\SogouC.reduced\\Reduced\\dictionary.txt", "G:\\Temp\\SogouC.reduced\\Reduced\\corpus.mm")
