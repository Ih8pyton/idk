#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def simple (arg):
        
    N = arg
    div = 2
    sqr = int(math.sqrt(arg))
    
    for i in range (1, N):
        if arg % div ==0:
            return False
        else: div=div+1
        if div > sqr:
            return True
            break
        
A=int(input())
print(simple(A))