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
        

num_to_factor = 600851475143
largest_factor = find_largest_factor(num_to_factor)
print largest_factor
