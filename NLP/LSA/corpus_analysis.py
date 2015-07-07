__author__ = 'chenzhi'

import matplotlib.pyplot as plt
import numpy as np
import math


def tmp(path):
    table = []
    with open(path, "r") as f:
        text = f.readlines()
    for line in text:
        tmp = line.strip().split("\t")
        table.append[tmp]
    print table

def plot_frequency_mapped(path):
    frequency_to_count_map = {}
    with open(path, "r") as f:
        text = f.readlines()
    for line in text:
        tmp = line.strip().split("\t")
        if int(tmp[2]) in frequency_to_count_map:
            frequency_to_count_map[int(tmp[2])] += 1
        else:
            frequency_to_count_map[int(tmp[2])] = 1
    frequency_to_count_table = frequency_to_count_map.items()
    sorted(frequency_to_count_table, key=lambda item: item[1])
    # change from list[tuple] to list[list], not necessary
    # frequency_to_count_table = [[item[0], item[1]] for item in frequency_to_count_table]
    print frequency_to_count_table
    frequency_to_count_matrix = np.array(frequency_to_count_table)
    plt.hist(frequency_to_count_matrix[:, 1], histtype='bar', rwidth=0.8)
    # print frequency_to_count_matrix[:,1]
    # plt.xlabel()
    plt.show()


def plot_frequency(path):
    frequency = []
    with open(path, "r") as f:
        text = f.readlines()
    for line in text:
        tmp = line.strip().split("\t")
        frequency.append(int(tmp[2]))
    frequency_matrix = np.array(frequency)
    bins = np.linspace(math.ceil(min(frequency)),
                   math.floor(max(frequency)),
                   50)
    plt.hist(frequency, bins, rwidth=0.8)
    plt.show()

if __name__ == "__main__":
    # plot_frequency("G:\\Temp\\SogouC.reduced\\Reduced\\dictionary.txt")
    tmp("G:\\Temp\\SogouC.reduced\\Reduced\\dictionary.txt")