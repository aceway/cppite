#!/usr/bin/env python
# -*- coding:utf-8 -*- tab:4
import os
import sys
import readline
from py import settings as sst
from py import utils
from py.cppite import CppIte

def main(argc, argv ):
    BASE_DIR    = os.path.dirname( os.path.abspath(os.path.dirname(__file__)) )
    os.chdir( BASE_DIR )
    print "\t{cs}Hello world! c++ Interactive Test Environment{ce}".format( cs=sst.color.FG_BLUE, ce=sst.color.END )
    try:
        readline.parse_and_bind("tab: complete")
        readline.parse_and_bind("set editing-mode emacs")
        ite = CppIte()
        cmd_idx = 0
        code_idx = 0
        ri = utils.get_raw_input(sst.root_tip, code_idx)
        while ( not utils.quit_ite( ri ) ):
            if ( ite.is_ite_cmd( ri ) ):
                ite.do_ite_cmd()
                cmd_idx += 1
            else:
                code_idx += 1
            ri = utils.get_raw_input( sst.root_tip, cmd_idx )
    except Exception,e:
        print e
if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
