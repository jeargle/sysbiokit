# John Eargle
# 2015

import sys
import json

import matplotlib.pyplot as plt
import numpy as np
# import sympy



def time_plot(duration):
    x = np.arange(0, duration, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

    return


class Product():

    def __init__(self):
        pass

    def plot(self):
        pass



if __name__=='__main__':
    time_plot(30)
