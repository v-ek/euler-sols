import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
# the number of NE (SE, NW, SW) paths in a NxN lattice is 2N choose N
print nCr(40,20)