#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Ïðîãðàììà, ïðîâåðÿþùàÿ ââåä¸ííîå ÷èñëî íà ïðîñòîòó"""

import math

def simple(arg):
    """Ðåàëèçîâàí àëãîðèòì ïåðåáîðà äåëèòåëåé"""
    N = arg
    div = 2
    sqr = int(math.sqrt(arg))
    for i in range(1, N):
        if arg % div == 0:
            return False
        else:
            div = div+1
        if div > sqr:  #ïðîâåðÿåì äî êîðíÿ èç ÷èñëà, âåäü îíî ìàêñèìóì ìîæåò áûòü êâàäðàòîì.
            return True

a = int(input())

print (simple(a))
