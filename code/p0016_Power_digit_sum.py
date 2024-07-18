"""
2^15 = 32768 and the sum of its digits is
3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

"""
Python can handle large integers very nice, so
this program is very short.
"""

from useful_funcs import digital_sum

def sum_of_digits():
    # Get the sum of the power of 2
    return digital_sum(2**1000)

print(sum_of_digits())