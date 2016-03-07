from __future__ import division

def find_largest_factor(num):
    i=1
    while True:
        i += 1
        if num % i == 0:
            if num == i:
                return num
            remainder = num // i
            next = find_largest_factor(remainder)
            return next

primes = []
num_of_primes = 10001
i = 2
while len(primes) < num_of_primes:
    max_factor = find_largest_factor(i)
    if max_factor == i:
        primes.append(i)
    i += 10001
