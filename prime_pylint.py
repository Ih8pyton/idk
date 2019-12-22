#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def simple(arg):  
    N = arg
    div = 2
    sqr = int(math.sqrt(arg))
    for i in range(1, N):
        if arg % div == 0:
            return False
        else: div = div+1
        if div > sqr:
            return True
            break
a = int(input())
print(simple(a))

"Your code has been rated at 2.86/10 (previous run: 2.14/10, +0.71).
 До использования PyLint'a оценка была в районе -2"
