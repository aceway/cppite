#!/usr/bin/env python
# -*- coding:utf-8 -*-

cmakelists_tmpl="""CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
SET(CMAKE_INCLUDE_DIRECTORIES_PROJECT_BEFORE  true)
SET(CMAKE_MODULE_PATH ${{CMAKE_MODULE_PATH}} "${{CMAKE_SOURCE_DIR}}/cmake/")
SET(EXECUTABLE_OUTPUT_PATH ${{CMAKE_SOURCE_DIR}}/../../bin/ )
SET(CMAKE_USE_RELATIVE_PATHS  true )
 
FIND_PACKAGE(glib REQUIRED)
 
INCLUDE_DIRECTORIES( 
    "/usr/include/"
    ${{GLIB_INCLUDE_DIR}}
    {add_include_dirs}
)
 
SET(SRC_PATH ./src/)
AUX_SOURCE_DIRECTORY(./src SRC_MAIN)

SET (SRC_LIST 
    ${{SRC_MAIN}}
)
 
SET(EXTRA_LIBS 
    glib-2.0
    ${{EXTRA_LIBS}}
    {add_static_libs}
)
 
ADD_EXECUTABLE(cppitehost ${{SRC_LIST}}   )

TARGET_LINK_LIBRARIES (cppitehost 
    ${{EXTRA_LIBS}}
)
 
ADD_DEFINITIONS("-Wall -MMD -g  -O2 -funroll-loops -z defs -DDEBUG -D__USE_STRING_INLINES -D_REENTRANT -D_GNU_SOURCE")
"""
