#!/usr/bin/env python
import sys
import settings as st
from src import settings as sst
from src import utils
from src.cppite import CppIte

def main(argc, argv ):
    print "\t{cs}Hello c++ Interactive Test Environment world!{ce}".format( cs=sst.color.FG_BLUE, ce=sst.color.END )
    try:
        ite = CppIte()
        idx = 0
        ri = utils.get_raw_input(sst.root_tip, idx)
        while ( not utils.quit_ite( ri ) ):
            if ( ite.parse_input( ri ) ):
                idx += 1
            ri = utils.get_raw_input( sst.root_tip, idx )
    #except Exception,e:
    except IOError,e:
        print e




if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
