#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gcd (a, b):
    if (b==0):
        return a
    else:
        return gcd (b, a % b)
    

def big_gcd(a,b):
    if (a==b):
        return (a, 1, 0)
    n = gcd (a,b)
    a1 = a/n
    b1 = b/n
    if (a1 > b1):
        a1 , b1 = b1, a1
    k = int(b1)
    u = 1
    for i in range (1, k):
        if (u*a1 % b1 == 1):
            v = int((1-u*a1)/b1)
            return (n,u,v)
        else: u=u+1
        

