from __future__ import division
import numpy as np

def get_next_collatz(num):
    if num % 2 != 0:
        return 3 * num + 1
    else:
        return num // 2

def get_collatz_seq(start):
    sequence = []
    next = start
    sequence.append(next)
    while True:
        if next == 1:
            break
        next = get_next_collatz(next)
        sequence.append(next)

    return (sequence)

collatz_seqs = []
lengths = []
for ii in range(1,1000001):
    collatz_seqs.append(get_collatz_seq(ii))

ctr = 0
for curr_list in collatz_seqs:
    length = len(curr_list)
    lengths.append(length)
    ctr += 1

max_value = max(lengths)
max_index = lengths.index(max_value)
#max index start from zero, but values starts from 1
print "Max starting index:"
print max_index + 1
print "Length:"
print max_value

