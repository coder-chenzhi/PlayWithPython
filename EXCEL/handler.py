# -*- coding: utf-8 -*-
__author__ = 'chenzhi'

from openpyxl import load_workbook
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def count_country():
    path = "G:\KuaiPan\Research\ByConferenceOrJournal\Conference\Cluster\Summary.xlsx"
    wb = load_workbook(filename=path, read_only=True)
    sheet = wb['2015']
    country_map = {}
    for row in sheet.rows:
        if row[4].value is None:
            continue
        if row[4].value in country_map:
            country_map[row[4].value] += 1
        else:
            country_map[row[4].value] = 1
        # print row[4].value
    for k in country_map:
        print k + '\t'.encode('utf-8') + str(country_map[k]).encode('utf-8')
    print "Done."


def plot():
    # set text size

    countries = u"America", u"China", u"France", u"Japan", u"Spain", u"Switzerland", u"Greece", u"Sweden", u"Austria", \
             u"Germany", u"Norway", u"Brazil"
    counts = [47, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
    sizes = [count*64.0/100.0 for count in counts]
    colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink',
              'darkgreen','yellow','grey','violet','magenta','cyan']
    # explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
    labels = ['{0} - {1}'.format(i,j) for i,j in zip(countries, counts)]

    zhfont = matplotlib.font_manager.FontProperties(fname='C:\\WINDOWS\\Fonts\\STSONG.TTF') #I am on OSX.

    patches, texts = plt.pie(sizes, colors=colors, shadow=False, startangle=90, radius=1.2)

    sort_legend = True
    if sort_legend:
        patches, labels, dummy = zip(*sorted(zip(patches, labels, sizes),
                                              key=lambda x: x[2],
                                              reverse=True))
    plt.legend(patches, labels, loc='center right',
           fontsize=16)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    plt.show()

if __name__ == "__main__":
    plot()
