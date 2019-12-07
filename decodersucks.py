#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def repeater(n):
    def facke_fun(genuine_function):
        def final_result(result):
            for i in range (n): 
                result = genuine_function(result)
            return result
        return final_result
    return facke_fun
                    
@repeater(2)
def plus_1(x):
    return x + 1
    
    
print(plus_1(3))