import math

iterations = 500000

def my_ln(x):
    """Вычисление логарифма при помощи частичного суммирования ряда Тейлора"""
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, iterations):
        x_pow *= x  
        multiplier *= -1 / (n+1) * n  
        partial_sum += x_pow * multiplier
    
    return partial_sum

print(help(math.log), math.log(2))
print(help(my_ln), my_ln(1))
