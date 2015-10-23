#!/usr/bin/env python
# -*- coding:utf-8 -*- tab:4
import sys
from py import settings as sst
from py import utils
from py.cppite import CppIte

def main(argc, argv ):
    print "\t{cs}Hello c++ Interactive Test Environment world!{ce}".format( cs=sst.color.FG_BLUE, ce=sst.color.END )
    try:
        ite = CppIte()
        idx = 0
        ri = utils.get_raw_input(sst.root_tip, idx)
        while ( not utils.quit_ite( ri ) ):
            if ( ite.is_cpp( ri ) ):
                idx += 1
            else:
                ite.do_ite_cmd()
            ri = utils.get_raw_input( sst.root_tip, idx )
    #except Exception,e:
    except IndexError,e:
        print e
if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
