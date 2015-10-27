#!/usr/bin/env python
# -*- coding:utf-8 -*- tab:4
import os
import sys
from py import settings as sst
from py import utils
from py.cppite import CppIte

def main(argc, argv ):
    BASE_DIR    =  os.path.abspath( os.path.dirname(__file__) )
    os.chdir( BASE_DIR )
    print "\t{cs}Hello c++ Interactive Test Environment world!{ce}".format( cs=sst.color.FG_BLUE, ce=sst.color.END )
    try:
        ite = CppIte()
        idx = 0
        ri = utils.get_raw_input(sst.root_tip, idx)
        while ( not utils.quit_ite( ri ) ):
            if ( ite.is_ite_cmd( ri ) ):
                ite.do_ite_cmd()
            else:
                idx += 1
            ri = utils.get_raw_input( sst.root_tip, idx )
    #except Exception,e:
    except IndexError,e:
        print e
if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
