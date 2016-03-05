from __future__ import division
import numpy as np

sum_of_squares = np.sum(np.arange(1,101) ** 2)
squared_sum = np.sum(np.arange(1,101)) ** 2

diff = squared_sum - sum_of_squares
print diff
