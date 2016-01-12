__author__ = 'chenzhi'

import matplotlib.pyplot as plt
import pandas as pd
import os

def read_directory(root_dir):
    """
    return all absolute path under root_dir
    :param root_dir: the root directory
    :return: a list of all file's under root directory
    """
    all_files = []
    for root, sub_dirs, files in os.walk(root_dir):
        for file_path in files:
            all_files.append(os.path.join(root, file_path))
    sorted(all_files)
    return all_files


def read_all_file(path_list, filename_filter=None):
    """
    return a map from filename to pandas object
    :param path_list: a list of file's absolute path
    :param filter: a lambda to filter file from filename, return value should be True or False
    :return: a map from filename to pandas object
    """
    data_map = {}
    for path in path_list:
        filename = path[path.rindex("\\") + 1:]
        if filename_filter is not None:
            if filename_filter(filename):
                data_map[filename] = pd.read_csv(path)
    return data_map


def plot(data_map, key):
    plt.plot(data_map[key]["value"])
    column_name = ""
    if "anomaly" in data_map[key].columns:
        column_name = "anomaly"
    else:
        column_name = "is_anomaly"
    for index, v in enumerate(data_map[key][column_name]):
        if v == 1:
            plt.scatter(index, data_map[key]["value"][index], s=30, c="red")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    files = read_directory("G:\Temp\ydata-labeled-time-series-anomalies-v1_0\A1Benchmark")
    data_map = read_all_file(files, lambda s: s.endswith("csv"))
    plot(data_map, "real_19.csv")