#!/usr/bin/env python
# -*- coding:utf-8 -*-
from settings import color
import commands
def quit_ite( input_str ):
    input_str = input_str.strip().upper()
    if input_str in ["QUIT", "EXIT", "BYE", "BYEBYE" ]:
        print "\t{cs}Exit c++ Interactive Test Environment now!{ce}".format( cs=color.FG_YELLOW, ce=color.END )
        return True
    else:
        return False

def get_raw_input(tip, idx):
    return raw_input("{t} [{i}]> ".format( t=tip, i=idx) )
