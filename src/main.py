#!/usr/bin/env python
# -*- coding:utf-8 -*- tab:4
import os
import sys
try:
    import readline
except ImportError,e:
    print "No readline module installed. {e}".format( e = e )
else:
    import atexit
    #import rlcompleter
from py import settings as sst
from py import utils
from py.cppite import CppIte

def main(argc, argv ):
    BASE_DIR    = os.path.dirname( os.path.abspath(os.path.dirname(__file__)) )
    os.chdir( BASE_DIR )
    print "\t{cs}Hello world! c++ Interactive Test Environment{ce}".format( cs=sst.color.FG_BLUE, ce=sst.color.END )
    try:
        histfile = os.path.join(os.path.expanduser("~"), ".his_cppite")
        try:
            readline.read_history_file( histfile )
        except IOError:
            pass
        atexit.register(readline.write_history_file, histfile)
        readline.parse_and_bind("tab: complete")
        readline.parse_and_bind("set editing-mode emacs")
        ite = CppIte()
        readline.set_completer( ite.completer )
        readline.set_completer_delims(" ")
        cmd_idx = 0
        code_idx = 0
        ri = utils.get_raw_input(sst.root_tip, code_idx)
        while ( not utils.quit_ite( ri ) ):
            if ( ite.is_ite_cmd( ri ) ):
                ite.do_ite_cmd()
                cmd_idx += 1
            else:
                code_idx += 1
            ri = utils.get_raw_input( sst.root_tip, code_idx )
        del histfile
    except KeyboardInterrupt,e:
        pass
    except EOFError,e:
        pass

if __name__ == "__main__":
    main( len(sys.argv), sys.argv )
