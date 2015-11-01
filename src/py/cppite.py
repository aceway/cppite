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
        self.include_files = []
        self.include_dirs = []
        self.is_verbose=False

        # command full name and its shortkeys
        self.ite_cmd_keymap={
            'RUN':      ("R", "RU"),
            'COMPILE':  ("C", "CO", "COM", "COMP"),
            'VERBOSE':  ("V", "VE", "VERB"),
            'SIMPLE':   ("S", "SI", "SIM"),
            'CLEAR':    ("CL", "CLE", ),
            'SHOW':     ("SH", "SHO", ),
            'HELP':     ("H",  "HEL", ),
            'CMD_CLEAR':     ("CCL", "CCLE", ),
            'CMD_HISTORY':   ("CH", "CHIS", ),
            'ADD_INCLUDE_FILE': ("AIF", ),
            'RM_INCLUDE_FILE':  ("RIF", "REMOVE_INCLUDE_FILE"),
            'ADD_INCLUDE_DIR':  ("AID", ),
            'RM_INCLUDE_DIR':   ("RID", "REMOVE_INCLUDE_DIR"),
            'LIST_INCLUDE_FILE':("LIF", ),
            'LIST_INCLUDE_DIR': ("LID", ),
        }
        

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
        cmd = self.ite_cmd[-1].strip().split(" ")
        ite_cmd=cmd[0].lower()
        args=cmd[1:]
        if cmd[0] in self.ite_cmd_keymap:
            ite_cmd=cmd[0].lower()
            args=cmd[1:]
        else:
            for k, v in self.ite_cmd_keymap.items():
                if cmd[0] in v:
                    ite_cmd=k.lower()
                    args=cmd[1:]
                    break
        if self.is_verbose:
            print "Do c++ ITE command:{c} {a}".format( c = ite_cmd, a=args )
        self._do_cmd( ite_cmd.lower(), args )


    def _do_cmd( self, cmd, *args, **keywords ):
        """
        Private command proxy, execute by command name rule."
        """
        if hasattr( self, "cmd_" + cmd.strip().lower() ) and callable( getattr(self, "cmd_" + cmd.strip().lower() ) ):
            func = getattr(self, "cmd_" + cmd.strip().lower() )
            try:
                ret = apply( func, *args, **keywords )
            except Exception, e:
                print "{e}".format( e = e )
                ret = None
            return ret
        else:
            print "{c}Not surpported command:{cmd}{e}".format( c=st.color.FG_RED, cmd=cmd, e=st.color.END )
            return None


    def cmd_help(self, name=None):
        """Print the cppite command help info."""
        if name  is None:
            print "{c}cppite command start with '#//' in the console line, here is all the supported commands:{e}"\
                    .format(c=st.color.FG_GREEN, e=st.color.END)
            cmds = [ c for c in dir(self) if c.startswith("cmd_") ]
            for c in cmds:
                sc = ",".join( self.ite_cmd_keymap[ c[4:].upper() ] )
                print "{c}: {s}. Short command:{sc}\n".format( c=c[4:], s=getattr(self, c).__doc__, sc=sc)
        else:
            name = name.lower()
            cmd_name = "cmd_{n}".format( n= name )
            if hasattr(self, cmd_name):
                sc = ",".join( self.ite_cmd_keymap[ name.upper() ] )
                print "{n}: {s}. Short command:{sc}".format( n=name, s= getattr(self, cmd_name).__doc__, sc=sc)
            else:
                print "{c}Not surpported command:{n}{e}".format( n=name, c=st.color.FG_RED, e=st.color.END )
                

    def cmd_cmd_history(self):
        """Show cppite commands history that you inputted before."""
        for cmd in self.ite_cmd[:-1]:
            print "{c}".format( c = cmd.strip() )


    def cmd_cmd_clear(self):
        """Clear cppite cached commands"""
        self.ite_cmd = []


    def cmd_verbose(self):
        """Run in verbose mode, print process detail info."""
        self.is_verbose = True


    def cmd_simple(self):
        """Run in simple mode, only print the result but no process info."""
        self.is_verbose = False


    def cmd_show(self):
        """Show the inputted c++ code that cached in cppite temp memory"""
        if self.is_verbose: print "{c}Show the cached c++ code:{e}".format( c=st.color.FG_GREEN, e=st.color.END )
        for c in self.cpp_fragment:
            print c


    def cmd_clear(self):
        """Clear the inputted c++ code that cached in cppite temp memory"""
        if self.is_verbose: print "{c}Clear the cached c++ code:\n{cd}\n{e}".format( c=st.color.FG_YELLOW, cd="\n".join(self.cpp_fragment), e=st.color.END )
        self.cpp_fragment = []


    def cmd_compile(self):
        """Compile the c++ code in cppite caching memory."""
        if self.is_verbose:
            print "Compile c++ code: {cpp}".format( cpp="\n".join(self.cpp_fragment) )
        self.gen_cpp_code_file()
        return self.exec_bash_cmd( st.compile_tool )


    def cmd_run(self):
        """Compile the inputted c++ code and run it"""
        if self.is_verbose:
            print "Run c++ code fragment: {cpp}".format( cpp="\n".join(self.cpp_fragment) )
        if os.path.isfile( st.out_bin_exe ):
            status, output = self.exec_bash_cmd( st.out_bin_exe )
            if status == 0: print output
        else:
            print "{c}Cannot find and gen {bf}!{e}".format( c=st.color.FG_RED, bf=st.out_bin_exe, e=st.color.END )
            

    def cmd_list_include_file(self):
        """List c++ include header files"""
        print "Now c++ include header file:"
        if len(self.include_files)==0: print "None"
        for hf in self.include_files:
            print hf


    def cmd_list_include_dir(self):
        """List c++ include header dirs"""
        print "Now c++ include header dir:"
        if len(self.include_dirs)==0: print "None"
        for hd in self.include_dirs:
            print hd

                  
    def cmd_add_include_file(self, *file_list):
        """Add c++ include header files"""
        if len(file_list) == 0: 
            print "Need header file name!"
        for f in file_list:
            if f in self.include_files:
                pass
            else:
                self.include_files.append(f)


    def cmd_add_include_dir(self, *dir_list):
        """Add c++ include header dirs"""
        if len(dir_list) == 0: 
            print "Need dir name!"
        for d in dir_list:
            if d in self.include_dirs:
                pass
            else:
                self.include_dirs.append(d)


    def cmd_rm_include_file(self, *file_list):
        """Remove c++ include header files"""
        for f in file_list:
            if f in self.include_files:
                self.include_files.remove(f)
            else:
                pass


    def cmd_rm_include_dir(self, *dir_list):
        """Remove c++ include header dirs"""
        for d in dir_list:
            if d in self.include_dirs:
                self.include_dirs.remove(d)
            else:
                pass

        
    def gen_cpp_code_file(self):
        """Use the input c++ code fragment(cached in the list) to generate c++ hpp/cpp file."""
        if self.is_verbose:
            print "Generating c++ code... {f}".format( f = st.cpp_code_dir )
        includes="#include <algorithm>\n"
        for f in self.include_files:
            includes += "#include <{f}>\n".format( f=f )
        hpp_code= hpp_tmpl.format( includes=includes )
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
