#!/usr/bin/env python
# -*- coding:utf-8 -*-

########################################################
# ITE command start with: #//
# ITE command keywords:quit,exit,byebye,bye, begin, end,
# verbose, concise, dump_project, dump_make_file, dump_cpp,
# dump_fragment,load_fragment, compile, run, edit
#
########################################################
import os
import commands
import settings as st
import utils as ut
from cpp_fragment_tmpl import hpp_tmpl, cpp_tmpl

class CppIte:
    def __init__(self):
        self.cpp_fragment = []
        self.ite_cmd = []
        self.is_verbose=False
        

    def is_ite_cmd(self, ri):
        """ Test wether the raw input is a ITE(interactive test environment) command
        or its c++ code fragment.
        """
        if ri.strip().startswith( "#//" ):
            self.ite_cmd.append( ri.strip().strip("#//").upper() )
            return True
        else:
            self.cpp_fragment.append( ri )
            return False


    def do_ite_cmd(self):
        """ Do the ITE command """
        if self.is_verbose:
            print "Do c++ ITE command:{c}".format( c = self.ite_cmd[-1] )

        if self.ite_cmd[-1] in ["R", "RU", "RUN"]:
            st, out = self._do_cmd( "compile" )
            if st == 0: self._do_cmd( "run" )
        elif self.ite_cmd[-1] in ["C", "COM", "COMP", "COMPILE" ]:
            self._do_cmd( "compile" )
        elif self.ite_cmd[-1] in ["V", "VE", "VER", "VERBOSE"]:
            self._do_cmd( 'verbose', (True, ) )
        elif self.ite_cmd[-1] in ["S", "SI", "SIM", 'SIMPLE']:
            self._do_cmd( 'verbose', (False,) )
        elif self.ite_cmd[-1] in ["CL", "CLE", "CLEAR" ]:
            self._do_cmd( 'clear' )
        else:
            self._do_cmd( self.ite_cmd[-1] )


    def _do_cmd( self, cmd, *args, **keywords ):
        """
        Private command proxy, execute by command name rule."
        """
        if hasattr( self, "cmd_" + cmd.strip().lower() ) and callable( getattr(self, "cmd_" + cmd.strip().lower() ) ):
            func = getattr(self, "cmd_" + cmd.strip().lower() )
            return apply( func, *args, **keywords )
        else:
            print "{c}Not surpport cmd:{cmd}.{e}".format( c=st.color.FG_RED, cmd=cmd, e=st.color.END )
            return None

    def cmd_verbose(self, verbose):
        self.is_verbose = True if verbose is True else False

    def cmd_clear(self):
        if self.is_verbose: print "{c}Clear the cached c++ code:\n{cd}\n{e}".format( c=st.color.FG_YELLOW, cd="\n".join(self.cpp_fragment), e=st.color.END )
        self.cpp_fragment = []


    def cmd_compile(self):
        """Generate the c++ code fragment.hpp/cpp files and compile them."""
        if self.is_verbose:
            print "Compile c++ code: {cpp}".format( cpp="\n".join(self.cpp_fragment) )
        self.gen_cpp_code_file()
        return self.exec_bash_cmd( st.compile_tool )


    def cmd_run(self):
        """ Compile the self.cpp_fragment(newest inputted) and run it"""
        if self.is_verbose:
            print "Run c++ code fragment: {cpp}".format( cpp="\n".join(self.cpp_fragment) )
        if os.path.isfile( st.out_bin_exe ):
            status, output = self.exec_bash_cmd( st.out_bin_exe )
            if status == 0: print output
        else:
            print "{c}Cannot find and gen {bf}!{e}".format( c=st.color.FG_RED, bf=st.out_bin_exe, e=st.color.END )

        
    def gen_cpp_code_file(self):
        """Use the input c++ code fragment(cached in the list) to generate c++ hpp/cpp file."""
        if self.is_verbose:
            print "Generating c++ code... {f}".format( f = st.cpp_code_dir )
        hpp_code= hpp_tmpl.format( includes="#include <algorithm>" )
        cpp_code = cpp_tmpl.format( head_file=st.hpp_filename, tmp_cpp= "\n".join(self.cpp_fragment) )
        with open( st.cpp_code_dir + st.hpp_filename, 'w') as hf:
            hf.write( hpp_code )
        with open( st.cpp_code_dir + st.cpp_filename, 'w') as cf:
            cf.write( cpp_code )


    def exec_bash_cmd(self, cmd):
        """
        Call the bash command or scripts, and get the return info.
        """
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
        if status != 0:
            print "{c}{out}{e}".format( c=st.color.FG_RED, out=output, e=st.color.END )
        elif self.is_verbose:
            print "{c}{out}{e}".format( c=st.color.FG_GREEN, out=output, e=st.color.END )
        return status, output
