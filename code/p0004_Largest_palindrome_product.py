"""
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
We check for pairs of numbers between 900 and 999 if their product is a
palindrome. After collecting all palindromes, we determine the maximum
and that is our solution.
"""

from itertools import combinations
from useful_funcs import is_palindrome

def sol():

    # We create a bunch of tuples of two elements of numbers between
    # 900 and 1000. 
    pairs = combinations(range(900, 1000), 2)

    # Extend those tuples with the product of the elements.
    pairs = [(a, b, a*b) for (a, b) in pairs]

    # Collect the tuples, where the product is a palindrome
    palins = set()
    for (a, b, c) in pairs:
        if is_palindrome(c):
            palins.add((a, b, c))
    
    # Find the tuple with the biggest product and return it
    return max(palins, key=lambda t : t[2])


print(sol())
