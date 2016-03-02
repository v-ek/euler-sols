from __future__ import division
# brute force again
f_all = []
f_even = []
even_sum = 0
max_val = 4000000

f_all.append(1)
f_all.append(1)
current = 0

while current < max_val:
    current = f_all[-1] + f_all[-2]
    f_all.append(current)
    if current % 2 == 0:
        f_even.append(current)
        even_sum += current

print even_sum