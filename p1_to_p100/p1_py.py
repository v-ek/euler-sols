from __future__ import division
#just go by brute force
total = 0
d1 = 3
d2 = 5
for i in range(1,1000):
    if i % d1 == 0 or i % d2 == 0:
        total += i
print total