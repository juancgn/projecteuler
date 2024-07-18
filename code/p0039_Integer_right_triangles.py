"""
If p is the perimeter of a right angle triangle with integral
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

"""
We loop over p and find out, which combinations of integer we can
use to keep the sum at p without repeating ourselve. For this, we
choose to let always be a < b. For c, we need c > 0 and between 1
and p. 

Therefore we loop a over 1 to p/2 - 1. Since b > a, a bigger value
would exceed p since p/2 + (p/2 + 1) > p. To ensure c > 0, we use
a loop for b from a+1 to p-a-1, so we have a+b = p-1 as maximum
and there is a space of one unit for c. 

We check if the generated triples are Pythagorean and if so, we
count them for this p. After finishing the loop, we just need to
find the maximum.
"""


def sol():
    # Here we store the foundet triples for every i
    pyth_trpl_cntrs = []
    for i in range(1001):

        # Triples for this i
        trpls = 0

        # Boundaries as explained above
        for a in range(1, i//2):
            for b in range(a+1, i-a):

                # Check if Pythagorean
                if a**2 + b**2 == (i-a-b)**2:
                    trpls += 1

        pyth_trpl_cntrs.append(trpls)

    # Return the index of the maximum
    return pyth_trpl_cntrs.index(max(pyth_trpl_cntrs)), 


print(sol())
