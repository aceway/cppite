#!/usr/bin/env python
# -*- encoding:utf-8 -*-

class CppIte:
    def __init__(self):
        pass
    def parse_input(self, ri):
        ri = ri.strip()
        if ri.startswith( "#//" ):
            return False
        else:
            return True
    
