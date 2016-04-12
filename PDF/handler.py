# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'chenzhi'


from PyPDF2 import PdfFileReader
import os


class Paper(object):
    def __init__(self):
        self.title = ""
        self.author_list = []
        self.pagenum = 0
        self.keywords = []
        self.institutions = []

    def __repr__(self):
        return self.title, "\"" + ",".join(self.author_list) + "\"", "\"" + ",".join(self.institutions) + "\"", \
            + "\"" + ",".join(self.keywords) + "\"", self.pagenum

    def __str__(self):
        return self.__repr__()


def read_directory(root_dir):
    all_files = []
    for root, sub_dirs, files in os.walk(root_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    sorted(all_files)
    return all_files


def page_count(obj):
    if isinstance(obj, str):
        pdf = PdfFileReader(open(obj, 'rb'))
        print pdf.getNumPages()
    elif isinstance(obj, list):
        page_map = {}
        for filename in obj:
            page = PdfFileReader(open(filename, 'rb')).getNumPages()
            if page in page_map:
                page_map[page] += 1
            else:
                page_map[page] = 1
        print "page\tcount:"
        for page in page_map:
            print str(page) + '\t' + str(page_map[page])


def author_count(obj):
    if isinstance(obj, list):
        author_map = {}
        for filename in obj:
            authors = PdfFileReader(open(filename, 'rb')).getDocumentInfo().author
            author_list = authors.split(", ")
            # print author_list
            for author in author_list:
                if author in author_map:
                    author_map[author] += 1
                else:
                    author_map[author] = 1
        print "author\tcount:"
        for author in author_map:
            print author.encode("utf-8") + '\t'.encode("utf-8") + str(author_map[author]).encode("utf-8")


def keyword_count(obj):
    if isinstance(obj, list):
        keyword_map = {}
        not_found = 0
        for filename in obj:
            keywords = PdfFileReader(open(filename, 'rb')).getDocumentInfo().getText("/Keywords")
            if keywords is None:
                not_found += 1
                continue
            keyword_list = keywords.split(", ")
            keyword_list = [keyword.lower() for keyword in keyword_list]
            # print author_list
            for keyword in keyword_list:
                if keyword in keyword_map:
                    keyword_map[keyword] += 1
                else:
                    keyword_map[keyword] = 1
        print "not found keywords", not_found
        print "keyword\tcount:"
        for keyword in keyword_map:
            print keyword.encode("utf-8") + '\t'.encode("utf-8") + str(keyword_map[keyword]).encode("utf-8")


if __name__ == "__main__":
    pdf_dir = "F:\\KuaiPan\\Lab\\Fund\\863服务开发包软件\\验收\\成果\\结题成果\\论文"
    all_files = read_directory(pdf_dir)
    all_pdf = [f for f in all_files if f.endswith(".pdf")]
    # keyword_count(all_pdf)
    for pdf in all_pdf:
        pdf_file = PdfFileReader(open(pdf, 'rb')).getDocumentInfo()
        print pdf_file.title