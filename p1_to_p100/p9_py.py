import numpy as np
#go by brute force again
coeff_sum = 1000
triplet = []

for a in range(1,1000):
    for b in range(a+1,1000):
        c = np.sqrt(a*a + b*b)
        if a + b + c == 1000:
            triplet.append(a)
            triplet.append(b)
            triplet.append(c)
            product = a * b * c
            break

print triplet, product