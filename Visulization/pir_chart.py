# -*- coding: utf-8 -*-
__author__ = 'chenzhi'

import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    matplotlib.rcParams['font.size'] = 20

    labels = u"大一", u"大二", u"大三", u"大四", u"硕士", u"博士", u"其他", u"毕业已工作"
    sizes = [16.67, 10.65, 13.43, 18.06, 9.26, 3.7, 3.7, 24.54]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink',  'peachpuff', 'papayawhip', 'whitesmoke']
    # explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

    zhfont = matplotlib.font_manager.FontProperties(fname='C:\\WINDOWS\\Fonts\\STSONG.TTF') #I am on OSX.

    wedges, _, _ = plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.2f%%', shadow=False, startangle=90, textprops={"fontproperties": zhfont})
    for wedge in wedges:
        wedge.set_alpha(0.5)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    plt.show()