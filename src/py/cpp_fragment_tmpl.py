#!/usr/bin/env python
# -*- coding:utf-8 -*-

hpp_tmpl="""#ifndef __FRAGMENT_HPP__
#define __FRAGMENT_HPP__

#include <string>
#include <vector>
#include <map>
#include <list>

// linux int type define; should be remore/add by system dependent in the future version.
#include <stdint.h>  

{includes}

void fragment_container();

#endif
"""

cpp_tmpl="""#include "{head_file}"
#include <iostream>
#include <stdio.h>

void fragment_container()
{{
  // tmp code begin
  {tmp_cpp}
  // tmp code end
}}
"""
