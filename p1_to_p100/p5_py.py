from __future__ import division

def factorize(num):
    factors=[]
    i=1
    while True:
        i += 1
        if num % i == 0:
            if num == i:
                return num
            factors.append(i)
            remainder = num // i
            next = factorize(remainder)
            if type(next) == int or type(next) == long:
                factors.append(next)
            else:
                factors.extend(next)
            return factors

all_factors = set()
for i in range(2,21):
    factors = factorize(i)
    print factors
