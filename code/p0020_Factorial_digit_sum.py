"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
"""
We compute it straight forward with our pre-defined functions.
"""

from useful_funcs import digital_sum
from math import factorial as fac

def sol():
    return digital_sum(fac(100))


print(sol())
