# the elegence of hamming is wild
import numpy as np
from functools import reduce
import operator as op
def ham_it(bits = None):
    if None or set(bits) == {0, 1}:
        bits = np.random.randint(0,2,16)
    n = reduce(op.xor, [i for i, bit in enumerate(bits) if bit])
    bits[n] = not bits[n]
    return bits
# I want to work on solomon reed lat