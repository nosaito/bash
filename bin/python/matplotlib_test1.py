#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
sys.path.append("/opc1/proteus/projects/scripts/MMJ_SRC/MMJ_LIB")

import argparse
import os
import os.path
import subprocess

#import mmjlib

from datetime import datetime, timedelta
import time



import numpy as np
import matplotlib.pyplot as plt



#
# test 1
#
def BasicPlot():
    x = np.random.randn(30)
    y = np.sin(x) + np.random.randn(30)

    #plt.plot(x, y, "o")  # "o"は小さい円(circle marker)
    plt.plot(x, y)
    #plt.show()

    x.sort()
    y.sort()

    plt.plot(x, y)
    plt.show()


#
# test 2
#
def DrawContour():
    delta = 0.1
    minXY=-5.0
    maxXY=5.0
    nContour=50

    def HimmelblauFunction(x,y):
        return (x**2+y-11)**2+(x+y**2-7)**2

    def CreateMeshData():
        x = np.arange(minXY, maxXY, delta)
        y = np.arange(minXY, maxXY, delta)
        X, Y = np.meshgrid(x, y)
        Z=[HimmelblauFunction(x,y) for (x,y) in zip(X,Y)]
        return(X,Y,Z)

    (X,Y,Z)=CreateMeshData()
    CS = plt.contour(X, Y, Z,nContour)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.show()






#
# main
#
#BasicPlot()
DrawContour()
