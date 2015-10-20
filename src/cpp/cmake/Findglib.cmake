FIND_PATH(GLIB_INCLUDE_PATH glib.h
        /usr/include/glib-2.0/
        /usr/local/include/glib-2.0/
        DOC "The directory where glib.h resides")

FIND_PATH(GLIB_CONFIG_INCLUDE_PATH glibconfig.h
        /usr/lib/glib-2.0/include/
        /usr/lib/x86_64-linux-gnu/glib-2.0/include/
        DOC "The directory where glib.h resides")

set (GLIB_INCLUDE_DIR ${GLIB_INCLUDE_PATH} ${GLIB_CONFIG_INCLUDE_PATH})

FIND_LIBRARY(GLIB_LIBRARY
        NAMES glib
        PATHS
        /usr/lib/x86_64-linux-gnu/
        /usr/local/lib/
        DOC "The GLIB library")

IF (GLIB_INCLUDE_DIR)
        SET( GLIB_FOUND 1 CACHE STRING "Set to 1 if Foo is found, 0 otherwise")
ELSE (GLIB_INCLUDE_DIR)
        SET( GLIB_FOUND 0 CACHE STRING "Set to 1 if Foo is found, 0 otherwise")
ENDIF (GLIB_INCLUDE_DIR)

MARK_AS_ADVANCED(GLIB_FOUND)

IF(GLIB_FOUND)
        MESSAGE(STATUS "FOUND: [glib]\t=> ${GLIB_INCLUDE_DIR}")
ELSE(GLIB_FOUND)
        MESSAGE(FATAL_ERROR "${BoldRed}NOT FOUND: ${BoldYellow}[glib]${ColourReset}\n\t${Green}Please try to install it: sudo apt-get install libglib2.0-dev, and then rm -rf ./build/*, and then recompile again.${ColourReset}")
ENDIF(GLIB_FOUND)
