cmake_minimum_required(VERSION 2.6)
SET (CMAKE_INCLUDE_DIRECTORIES_PROJECT_BEFORE  true)
SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")
#SET(CMAKE_INSTALL_PREFIX "/usr/local")
SET(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/../../bin/ )
SET(CMAKE_USE_RELATIVE_PATHS  true )
 
find_package(glib REQUIRED)
 
INCLUDE_DIRECTORIES( 
    "/usr/include/"
    "/usr/local/include/"
    ${GLIB_INCLUDE_DIR} )
 
SET(SRC_PATH ./src/)
aux_source_directory(./src SRC_MAIN)

SET (SRC_LIST 
    ${SRC_MAIN}
)
 
add_definitions("-Wall -MMD -g  -O2 -funroll-loops -z defs -DDEBUG -D__USE_STRING_INLINES -D_REENTRANT -D_GNU_SOURCE")
 
 
set (EXTRA_LIBS ${EXTRA_LIBS} glib-2.0 m )
 
add_executable(cppitehost ${SRC_LIST}   )
 
target_link_libraries (cppitehost ${EXTRA_LIBS})
 
