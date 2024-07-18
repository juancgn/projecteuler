"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
We simply try all possible triples of numbers, which sums up to 1000 and
check if they're Pythagorean.
"""

def generate_pythagorean_triple():
    n = 1000

    # Loop over all numbers below n
    for a in range(1, n):

        # a and b are interchangable, so we just need to check bigger numbers
        for b in range(a, n):

            # Get the third number, which must add to 1000
            c = n-a-b

            # If this triple is Pythagorean, we finished
            if a*a + b*b == c*c:
                return (a, b, c)


print(generate_pythagorean_triple())
