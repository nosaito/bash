#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
sys.path.append("/opc1/proteus/projects/scripts/MMJ_SRC/MMJ_LIB")

#import argparse
#import os
#import os.path
#import subprocess

from pylab import *
from pandas import *

import numpy as np
import matplotlib.pyplot as plt


#x = np.arange(-3,3,0.1)
#y = np.sin(x)
#plt.plot(x,y)

#x=np.random.randn(30)
#y=np.sin(x)+np.random.randn(30)
#plt.plot(x,y,"o")


ts = Series(randn(1000), index=date_range('1/1/2000',periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
plt.savefig("image.png")
