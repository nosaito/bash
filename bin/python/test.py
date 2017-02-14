#!/usr/bin/env python
# -*- coding: utf8 -*-

# case in Python 2.6~
# same print behavior as python 3
from __future__ import print_function

import sys
sys.path.append("/opc1/proteus/projects/scripts/MMJ_SRC/MMJ_LIB")

import argparse
import os
import os.path
import subprocess

##import mmjlib

from datetime import datetime, timedelta
import time



parser = argparse.ArgumentParser()
parser.add_argument("param1", help='first option', nargs='?')  # not required parameter
parser.add_argument("param2", help='second option', nargs='?')
args = parser.parse_args()

def run():
    test1()  # here document
    #test2()  # subprocess
    #test3()  # hash for "for"  *need mmjlib.py
    #test4()  # split_param_list test
    #test5()   # time test


#
# here document test
#
def test1() :
    s1 = "world"
    s2 = "warcraft"
    s  = """\
this
is
a
test {s1}
data {s2}""".format(**vars())
    print(s)


def test2():
    s = subprocess.check_output( "ls -l | grep test", shell=True ).decode('utf-8')
    s1 = s.splitlines()

    for s2 in s1:
        print ( "file: " + s2 )


def test3():
    if args.param1:
        params = mmjlib.read_ppc_setting_file(args.param1)

        for key, value in params.items() :
            if "{" in value :
                pass
                print (key + ":")
                print (mmjlib.split_param_list(value))
            else:
                pass
                print (key + "--" + value)
    else:
        print ('ERROR: target param is not specified.')


def test4():
    param = '{"ptag_nv_Nominal W<60.0 400.0<=C 1.5<E" "ptag_nv_Nominal 60.0<=W<400.0 400.0<=C 1.3<=E" }'
    arg = mmjlib.split_param_list( param )
    print (arg)


def test5():
    t  = time.time()
    t1 = datetime.now()
    for i in range(10000):
        pass
    t2 = datetime.now()
    td = t2 - t1
    t0 = datetime(*time.localtime(t)[:6])
    print ( "time1: "      + t1.strftime('%Y/%m/%d %H:%M:%S') )
    print ( "time2: "      + t2.strftime('%Y/%m/%d %H:%M:%S') )
    #print ( "delta time: " + td.strftime('%Y/%m/%d %H:%M:%S'))

run()
