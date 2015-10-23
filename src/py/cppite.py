#!/usr/bin/env python
# -*- coding:utf-8 -*-

########################################################
# ITE command start with: #//
# ITE command keywords:quit,exit,byebye,bye, begin, end,
# verbose, concise, dump_project, dump_make_file, dump_cpp,
# dump_fragment,load_fragment, compile, run, edit
#
########################################################
import commands
import settings as st
import utils as ut
from cpp_fragment_tmpl import hpp_tmpl, cpp_tmpl

class CppIte:
    def __init__(self):
        self.cpp_fragment = []
        self.ite_cmd = []
        self.out_put_mode="SIMPLE"
        
    def is_cpp(self, ri):
        """ Test wether the raw input is c++ code fragment,
        or it is a ITE(interactive test environment) command
        """
        raw_ri=ri
        ri = ri.strip()
        if ri.startswith( "#//" ):
            self.ite_cmd.append( ri.strip("#//").upper() )
            return False
        else:
            self.cpp_fragment.append( raw_ri )
            return True

    def compile_run(self):
        """ Compile the self.cpp_fragment(newest inputted) and run it"""
        if self.out_put_mode == "VERBOSE":
            print "Compile & run c++ code: {cpp}".format( cpp="\n".join(self.cpp_fragment) )
        self.gen_cpp_code_file()
        out_put = self.exec_bash_cmd( st.compile_tool )
        if self.out_put_mode == "VERBOSE":
            print out_put

    def do_ite_cmd(self):
        """ Do the ITE command self.ite_cmd(newest inputted)"""
        if self.out_put_mode=="VERBOSE":
            print "Do c++ ITE command:{c}".format( c = self.ite_cmd[-1] )
        if self.ite_cmd[-1] in ["R", "RU", "RUN"]:
            print self.exec_bash_cmd( st.out_bin_exe )
        elif self.ite_cmd[-1] in ["C", "COM", "COMP", "COMPILE" ]:
            self.compile_run()
        else:
            print "cppite unknown cmd:{c}!".format( c=self.ite_cmd[-1] )
        
    def gen_cpp_code_file(self):
        if self.out_put_mode=="VERBOSE":
            print "Generating c++ code... {f}".format( f = st.cpp_code_dir )
        hpp_code= hpp_tmpl.format( includes="#include <algorithm>" )
        cpp_code = cpp_tmpl.format( head_file=st.hpp_filename, tmp_cpp= "\n".join(self.cpp_fragment) )
        with open( st.cpp_code_dir + st.hpp_filename, 'w') as hf:
            hf.write( hpp_code )
        with open( st.cpp_code_dir + st.cpp_filename, 'w') as cf:
            cf.write( cpp_code )

    def exec_bash_cmd(self, cmd):
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
