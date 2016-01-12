__author__ = 'chenzhi'

import os

FILE_DIRECTORY = "G:\Temp\ExportData"


def preprocess():
    """
    sort all records by probekey and time
    :return:
    """
    file_list = sorted([name for name in os.listdir(FILE_DIRECTORY) if name.endswith('.csv')])
    for fname in file_list:
        with open(fname, "r") as f:
            pass