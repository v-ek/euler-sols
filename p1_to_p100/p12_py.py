from __future__ import division
import numpy as np

def get_triangle_num(num):
    return int(num * (num + 1) / 2)

def get_divisors(num):
    divisors = []
    curr_divisor = int(np.floor(num/2))
    
    while True:
        if curr_divisor == 1:
            divisors.append(1)
            break
        elif num % curr_divisor == 0:
            divisors.append(curr_divisor)
        curr_divisor -= 1

    return divisors

def factorize(num):
    factors=[]
    i=1
    while True:
        i += 1
        if num % i == 0:
            if num == i:
                return [num]
            factors.append(i)
            remainder = num // i
            next = factorize(remainder)
            if type(next) == int or type(next) == long:
                factors.append(next)
            else:
                factors.extend(next)
            return factors

tresh = input("Treshhold for number of factors: ")
i = 2
while True:
    curr_triangle_num = get_triangle_num(i)
    prime_divisors = np.array(factorize(curr_triangle_num))
    divisor_counts = np.bincount(prime_divisors)
    exp_p1 = divisor_counts[divisor_counts.nonzero()] + 1
    prod = exp_p1.prod()
    if prod > tresh:
        break
    i += 1

print curr_triangle_num
