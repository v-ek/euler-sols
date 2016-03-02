from __future__ import division
import numpy as np
# brute force again
def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

product = 600851475143
divisor_start = int(np.floor(np.sqrt(product)))
print max_divisor
for divisor in range(max_divisor,product):
    if product % divisor == 0:
        quotient = int(product / divisor)
        if is_prime(quotient):
            print quotient
            break
 

