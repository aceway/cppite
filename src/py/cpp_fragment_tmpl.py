#!/usr/bin/env python
# -*- coding:utf-8 -*-

hpp_tmpl="""
#include <string>
{includes};

void fragment_container();
"""

cpp_tmpl="""
#include "{head_file}"
#include <iostream>

void fragment_container()
{{
  // tmp code begin
  {tmp_cpp}
  // tmp code end
}}
"""
