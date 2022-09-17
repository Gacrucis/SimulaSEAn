from main import *
from distributions import *

from matplotlib import pyplot as plt

from numpy import random


# print([n for n in range(day_start+shift_delta, day_end+shift_delta, shift_delta)])

# vals = []
# for n in range(1000):
    # vals.extend(poisson_hom(120, 3))
    # vals.extend(poisson(12, 50))
    # vals.extend(random.poisson(0.7, 20))
    # vals.append(len(poisson(2, 50)))
    # vals.append(len(poisson_hom(2, 0.01)))

# def lamt(t):
#     if t < 2:
#         return 5
    
#     return 20 - (t - 2) / 1

k = 24
vals = [n * 12 / k for n in poisson_var(k)]
# vals = pp(20, 5)
plt.hist(vals)
plt.show()