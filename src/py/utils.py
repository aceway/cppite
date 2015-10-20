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

def exec_bash_cmd(cmd):
    the_data = {}
    cmd = "{sh} ".format(sh=cmd)
    (status, output) = commands.getstatusoutput(cmd)
    if status == 0:          
        the_data['code'] = 0 
        the_data['data'] = output
        the_data['desc'] = "OK"
    else:                    
        info = output.split(" ")
        new_info = []        
        # 屏蔽密码           
        for d in info:       
            if len(d) > 2 and d.lower().startswith("-p"):
                d = "-p******"
            elif len(d) > 2 and d.lower().startswith('"-p'):
                d = "-p******"
            elif len(d) > 2 and d.lower().startswith("'-p"):
                d = "-p******"
            else:            
                d = d        
            new_info.append(d)
        output = " ".join(new_info)
        the_data['code'] = -1
        the_data['data'] = "<br>{op}".format(op=output)
        the_data['desc'] = "{op}".format(op=output)
    return output
