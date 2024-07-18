"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

"""
We find all abundant numbers by brute-forcing them and use the Cartesian
product of this set to create pairs of them. Then, we compute the sums
and we get all abundant sums in our range. Building the set difference
with the set of all numbers in our range, we get all non-abundant numbers.
"""
from useful_funcs import get_all_divisors
from itertools import product


def get_non_abundant_sums():

    # Check if a number is abundant by computing it explicitly
    def is_abundant(n):
        return n < sum(get_all_divisors(n).difference({n}))
    
    # Create a set of all abundant list below
    abundant_numbers = {i for i in range(1, 28124) if is_abundant(i)}

    # Create pairs of abundant numbers, including pairs with two identical numbers (Cartesian product)
    pairs_of_abundant_numbers = product(abundant_numbers, abundant_numbers)

    # Add up the numbers of the pairs - those are the abundant sums
    abundant_sums = {sum(pair) for pair in pairs_of_abundant_numbers}

    # Get a set of all non-abundant sums by computing the difference of the sets
    non_abundant_numbers = set(range(1, 28124)).difference(abundant_sums)

    # Return the sum of the non-abundant numbers
    return sum(non_abundant_numbers)


print(get_non_abundant_sums())
