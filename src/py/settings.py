#!/usr/bin/env python
# -*- coding:utf-8 -*-
class color:
    FG_BLAcK    = "\033[30m"    # 将字符的显示颜色改为黑色
    FG_RED      = "\033[31m"    # 将字符的显示颜色改为红色
    FG_GREEN    = "\033[32m"    # 将字符的显示颜色改为绿色
    FG_YELLOW   = "\033[33m"    # 将字符的显示颜色改为黄色
    FG_BLUE     = "\033[34m"    # 将字符的显示颜色改为蓝色
    FG_PINK     = "\033[35m"    # 将字符的显示颜色改为紫色
    FG_WHITE    = "\033[37m"    # 将字符的显示颜色改为灰色
    FG_LIGHT_BLUE= "\033[36m"   # 将字符的显示颜色改为淡蓝色
    
    BG_BLACK    = "\033[40m"    # 将背景色设置为黑色
    BG_RED      = "\033[41m"    # 将背景色设置为红色
    BG_GREEN    = "\033[42m"    # 将背景色设置为绿色
    BG_YELLOW   = "\033[43m"    # 将背景色设置为黄色
    BG_BLUE     = "\033[44m"    # 将背景色设置为蓝色
    BG_PINK     = "\033[45m"    # 将背景色设置为紫色
    BG_WHITE    = "\033[47m"    # 将背景色设置为灰色 
    BG_LIGHT_BLUE= "\033[46m"  # 将背景色设置为淡蓝色=    
    END         ="\033[0;00m" 



root_tip="{cs}CPPITE {ce}".format( cs=color.FG_GREEN, ce=color.END )
compile_tool="./bin/COMPILE"
out_bin_exe="./bin/cppitehost"

cpp_code_dir="./src/cpp/src/"
hpp_filename="fragment.hpp"
cpp_filename="fragment.cpp"

cmakelists_dir="./src/cpp/"
cmakelists_filename="CMakeLists.txt"

default_include_headers=[
    "vector",
    "map",
    "list",
    "algorithm"
]

default_include_dirs=[
    "/usr/local/include/",
]

default_static_files=[
]

default_static_dirs=[
]
