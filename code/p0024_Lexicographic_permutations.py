"""
A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of
0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

"""
We create all permutations of the digits 0-9. As we
give them is a ascending order, python gives us the
permutations in a ascending order back, therefore they
are in a lexicographic order as desired.
"""

from itertools import permutations

def sol():
    # Create permutations
    p = permutations("0123456789")

    # Get the millionth permutation
    return list(p)[1000000-1]


print(sol())
