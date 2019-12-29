#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Программа, проверяющая данное число на простоту"""

import math

def simple(arg):
    """Реализован алгоритм перебора делителей"""
    N = arg
    div = 2
    sqr = int(math.sqrt(arg))
    for i in range(1, N):
        if arg % div == 0:
            return False
        else:
            div = div+1
        if div > sqr:  #Проверяем до корня из числа
            return True

a = int(input())

print (simple(a))
