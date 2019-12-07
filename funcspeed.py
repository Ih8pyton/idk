#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)

for n in range(1, 10):
    print(n, fib_1(n))


    from timeit import Timer
    t = Timer(lambda: fib_1(n))
    print (t.timeit(number=1))

import functools

@functools.lru_cache()
def fib_2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)

for n in range(1, 10):
    print(n, fib_2(n))
    
    from timeit import Timer
    t = Timer(lambda: fib_2(n))
    print (t.timeit(number=1))

""" для fib_1(10) время выполнения равно 9.459996363148093e-06
    для fib_2(10) время выполнения равно 3.600012860260904e-06 
    время немного скачет при повторном использовании функции,
    скорее всего это зависит ещё и от возможностей компьютера,
    но в среднем скорость отличается примерно в 2,5 - 3 раза"""
