"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
https://projecteuler.net/project/images/p015.png
How many such routes are there through a 20×20 grid?
"""

"""
This problem can be considered as follows. Let (l_1, ..., l_40), l_i = r or l_i = d, where r stands
for a step right and d for a step down. Those tuples represents a route through the grid.
Now, we need to know how many tuples there are to determine the possible routes through the grid.

This is a combinatorical problem of permutation with repitition. First, there are 40! possible
ways of how to order 40 different elements. Since 20 of them are r, there are 20! possible
equivalents of those tuples. For every of those equivalents, there are 20! equivalents for
d since changing their positions does not have an effect. Hence, we have 40! / (20! * 20!)
possible tuples in this case and therefore as many routes through the grid.

However, despite its mathematical precision, this formula is inconvinient from a numerical
perspective, since we compute 40! and divide by 20!. To avoid this, we define a function,
which shorten this computation by just multiplying the necessary numbers and get our solution
with (40!/20!) * 1/20!.
"""

from math import factorial as fac

def lattice_paths():
    # Define a function, which computes the division of two factorials
    def fac_div(num, denom):
        k = 1
        for i in range(denom+1, num+1):
            k*=i
        return k

    # Compute (40!/20!) / 20!
    n = fac_div(40, 20)
    m = fac(20)
    
    return n // m


print(lattice_paths())
