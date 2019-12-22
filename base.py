#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def to_str(arg):
    if arg < 10:
        return chr(arg + ord('0'))
    else: return chr(arg + ord('A') - 10)

def anti_int(a, b):
    str = ""
    while a != 0:
        c = a % b
        str += to_str (c)
        a = a // b
    return "".join(reversed(str))
    
    
m = int(input())
n = int(input())

print(anti_int(m, n))
            
            