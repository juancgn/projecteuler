"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly
once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime
that exists?
"""

"""
We create all permutations, iterate from 7654321
down to 12 until we found a prime number.
As 1+2+...+8=33 and 1+2+...+8+9=42 are divisible by
3, every 9-digit pandigital is divisible by 3; so
we start with 7-digit pandigitals.

First, we create all permutations of the 7 digits.
This list can be recycled, as the permutations of
the digits 1, ..., k can be extracted from the last
k elements of the permutation, of the first k!-1
permutations.
"""
from itertools import permutations
from math import factorial as fac
from useful_funcs import is_prime


def sol():
    # All permutations of 7 digits
    perms_tuples = list(permutations("7654321"))

    # Check pandigitals of length k
    for k in range(7, 2, -1):

        # As perms_tuples is sorted, the last k elements of
        # the first k!-1 permutations are all permutations
        # of 1, ..., k (sorted!)
        for p in perms_tuples[0:fac(k)]:

            # Get the last k elements
            t = p[-k:]

            # Convert string to int
            n = int("".join(t))

            if is_prime(n):
                return n


print(sol())
