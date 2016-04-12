# -*- coding: utf-8 -*-
__author__ = 'chenzhi'

import sys
type = sys.getfilesystemencoding()


def read_file(file_path):
    """
    read specific file and return list of lines
    :param file_path:
    :return:
    """
    with(open(file_path, "r")) as f:
        file_content = f.readlines()
    return file_content


def delete_authors_abbr(file_content):
    print_flag = True
    for line in file_content:
        if line.decode("UTF-8").startswith("AU"):
            print_flag = False
        elif line.decode("UTF-8").startswith(u"作者"):
            print_flag = True

        if print_flag:
            print(line.decode("utf-8").encode(type).replace("\n", ""))


def delete_editors(file_content):
    print_flag = True
    for line in file_content:
        if line.decode("UTF-8").startswith("BE"):
            print_flag = False
        elif line.decode("UTF-8").startswith(u"标题"):
            print_flag = True

        if print_flag:
            print(line.decode("utf-8").encode(type).replace("\n", ""))


def get_all_records_for_specific_correspond_author(file_path, author):
    """
    each record should be separated by one empty line
    :param file_content: list of lines
    :param author: name of specific author
    :return:
    """
    file_content = file(file_path).read()
    records = file_content.split("\n\n")
    for record in records:
        if u"通讯作者：" + author in record.decode("utf-8"):
            print record.decode("utf-8").encode(type) + '\n'


def get_all_records_for_specific_first_author(file_path, author):
    """
    each record should be separated by one empty line
    :param file_content: list of lines
    :param author: name of specific author
    :return:
    """
    file_content = file(file_path).read()
    records = file_content.split("\n\n")
    for record in records:
        if u"第一作者：" + author in record.decode("utf-8") and \
              u"通讯作者：" + author not in record.decode("utf-8"):
            print record.decode("utf-8").encode(type) + '\n'

def get_all_records_for_not_first_and_correspond_author(file_path, author):
    """
    each record should be separated by one empty line
    :param file_content: list of lines
    :param author: name of specific author
    :return:
    """
    file_content = file(file_path).read()
    records = file_content.split("\n\n")
    for record in records:
        if u"第一作者：" + author not in record.decode("utf-8") and \
              u"通讯作者：" + author not in record.decode("utf-8"):
            print record.decode("utf-8").encode(type) + '\n'


def add_order(file_path):
    file_content = file(file_path).read()
    records = file_content.split("\n\n")
    for i, record in enumerate(records):
        print str(i + 1) + "."
        print record.decode("utf-8").encode(type) + "\n"


if __name__ == "__main__":
    file_path = u"F:\KuaiPan\Lab\Fund\杰青\\2016.2.25_图书馆\SCI 统计.txt"
    file_content = read_file(file_path)
    # delete_authors_abbr(file_path)
    # delete_editors(file_content)
    # get_all_records_for_specific_first_author(file_path, u"尹建伟")
    get_all_records_for_not_first_and_correspond_author(file_path, u"尹建伟")