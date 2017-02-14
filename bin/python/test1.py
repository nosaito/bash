#!/usr/bin/env python
# -*- coding: utf8 -*-


# case in Python 2.6~
from __future__ import print_function  # same print behavior as python 3
from __future__ import division        # same division behavior for python 3/2

import argparse
import os
import os.path
import re          # regular expression
import fileinput


### argparse
parser = argparse.ArgumentParser()
parser.add_argument("param1", help='target dir')            # required parameter
parser.add_argument('-mode', type=str, choices=['chk_rounding','chk_dbu','find_postopc'], help='mode option')  # flag option
parser.add_argument('--version', action='version', version='%(prog)s 2.0') # version
args = parser.parse_args()


global global_param

print ("test")


###
### Main routine
###



###
### Main routine
###


#
#
#
def list_files_from_current_dir_sub( tgt ):
    file_list = os.listdir(tgt)

    for i in file_list:
        file_path = tgt + "/" + i
        isJcf = re.search( r".jcf", file_path )

        if os.path.isdir( file_path ) == True:
            list_files_from_current_dir_sub( file_path )

        elif isJcf :
            check_jcffile( file_path )

        else:
            pass
        #   print (file_path)
    return 0


#
#
#
def check_jcffile( tgt ):
    global global_param
    global_param = read_ppc_setting_file( tgt, "" )

    #for s in param:
    #    print( "  " + s + " = " + param[s] )

    if ( not 'jcf::outputGdsGrid' in global_param ):
        print ("jcf: " + tgt, end="  ")
        #print( "  jcf::outputGdsGrid = " + param['jcf::outputGdsGrid'] )
        print ( "scale/input/type = " + jcfstr('jcf::inputGdsScaleFactor') + '/' \
                                      + jcfstr('jcf::inputGdsGrid') + '/' \
                                      + jcfstr('jcf::outputGdsScaleType') )
    return 0


#
#
#
def jcfstr( str ):
    if str in global_param:
        return global_param[str]
    else:
        return "---"


#
#
#
def read_ppc_setting_file( filename, *mode ):

    param = {}

    fh = open(filename, 'r')

    #for cl in fileinput.input(filename):
    for cl in fh :
        cl_org = cl
        cl.lstrip  # remove spaces on the beginning of the line and CR.
        if re.match("set", cl):

            args = re.split(" +", cl)
            args = map(str.rstrip, args)   # remove CR

            if len(args) <= 2 :
                param[args[1]] = ""

            elif not re.match("{", args[2]) :
                param[args[1]] = args[2]

            else :
                cl = cl_org
                cl.rstrip
                cl = re.sub( '^\s*\w+\s+[\w:]+\s+' , '', cl )  # remove " set [arg_name] ";
                cl = re.sub( ';.+$'                , '', cl )  # remove comment

                if not re.match( "{", cl ) :  # if not include "}"
                    isEnd = 0
                    while not isEnd :
                        cl2 = fh.readline()
                        cl2.rstrip
                        cl += cl2
                        if re.match( '}', cl2 ) :
                            isEnd = 1
                param[args[1]] = cl

    fh.close()

    if "also_param" in mode :
        paramfile = param['jcf::paramFile']
        paramfile = os.path.basename(filename) + "/" + paramfile
        param_args = read_ppc_setting_file( paramfile, "" )
        param.update( param_args )
        #$param{version} = &GetVersionFromRecipeFile($paramfile);

    return param





IGNORE_DIR_LIST = [ 'aptina', '3DSGM', 'agrate', 'tachyon', 'tapeout', 'tmod', 'design', 'dfm', 'frame', 'mfill', 'pad_log', 'sivl', 'tmp' ]

#
#
#
def find_postopc( tgt ):
    global postopc_list

    file_list = os.listdir(tgt)
    #outbox = '/home/central_data/flash/100/l04a/opc/'

    for i in file_list:
        file_path = tgt + "/" + i

        if i in IGNORE_DIR_LIST or "agrate" in i or i[0]=='.':
            pass

        elif os.path.isdir( file_path ) == True:
            #print ("dir: " + file_path)
            find_postopc( file_path )

        elif re.search( "postopc\d.oas\Z", i ) or re.search( "postopc\d.oas.WARP.locked\Z", i ) :
            postopc_list.append(file_path)

        else:
            pass
        #   print (file_path)
    return 0




###
### Main routine
###



# usage1: -mode chk_dbu <tgt_dir>
if  args.mode=="chk_dbu" :
    list_files_from_current_dir_sub( args.param1 )

# usage2: -mode find_postopc
elif args.mode=="find_postopc" :
    # get preopc list
    #inbox = '/proj/dppg/opc/inbox'
    #preopc_list = os.listdir(inbox)
    #print (preopc_list)

    # get postopc list
    # sample: '/home/central_data/dram/100/z01b/opc/z01b0076_91D_L__die001_postopc1.oas.WARP.locked'
    postopc_list = []
    FIND_LIST = ( 'dram-110-45', 'dram-120-22', 'dram-120-29', 'dram-120-20', 'dram-120-49', 'dram-130-29', 'dram-130-49',)
    outbox = '/home/central_data'
    find_postopc( outbox )  # result -> postopc_list
    for i in postopc_list :
        s = i.split("/")
        #type, node, part = s[2:4]
        type = s[3]
        node = s[4]
        part = s[5]
        file = s[7]
        layer = file[9:11]
        typestr = type + '-' + node + '-' + layer

        if typestr in FIND_LIST :
            print ( typestr + ' : ' + i )
