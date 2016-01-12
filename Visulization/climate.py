__author__ = 'chenzhi'

import numpy as np
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # Chicago
    low = np.array([-7.7, -5.7, -0.6, 5.4, 10.9, 16.7, 19.7, 19, 14.2, 7.6, 1.4, -5.2])
    high = np.array([-0.3, 2.1, 8.2, 15.1, 21.2, 26.6, 29, 27.8, 24.1, 17.1, 9.2, 1.8])

    # Hangzhou
    low = np.array([1.8, 3.5, 7.0, 12.4, 17.5, 21.4, 25.2, 24.9, 20.9, 15.4, 9.3, 3.7])
    high = np.array([8.3, 10.3, 14.8, 21.1, 26.3, 29.1, 33.6, 32.8, 28.2, 23.2, 17.3, 11.3])
    ind = np.arange(12)

    plt.xlim([0, 13])
    plt.ylim([-10, 40])
    plt.gca().grid(True)
    plt.plot(range(1, low.shape[0]+1), low, '-', marker='o', markersize=6, color='blue', label='Average Low')
    plt.plot(range(1, low.shape[0]+1), high, '-', marker='o', markersize=6, color='red', label='Average High')
    xticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.xticks(range(1, low.shape[0]+1), xticks, fontsize=10)
    plt.legend()
    plt.title("Hangzhou Climate")
    plt.show()
