#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

iterations = 5000

def my_ln(x: float) -> float:
    """Вычисление логарифма при помощи частичного суммирования ряда Тейлора"""
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, iterations):
        x_pow *= x  
        multiplier *= -1 / (n+1) * n  
        partial_sum += x_pow * multiplier
    
    return partial_sum

print(math.log(2))
print(my_ln(1))
