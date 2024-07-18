"""
It is possible to show that the square root of
two can be expressed as an infinite continued
fraction.

\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}

By expanding this for the first four iterations, we get:

1 + \frac 1 2 = \frac  32 = 1.5
1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4
1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots
1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots

The next three expansions are 99/70, 239/169 and 577/408,
but the eighth expansion, 1393/985, is the first example
where the number of digits in the numerator exceeds the
number of digits in the denominator.

In the first one-thousand expansions, how many fractions
contain a numerator with more digits than the denominator?
"""

"""
To solve this problem, we need to compute every element
and consider their representation as a fraction. As the
fraction seems like it could be computed with recursion
well, this might be a first approach. However, a problem
occurs when computing such deep recursions (RecursionError).
The call stack overflows in that case.

To avoid this, we use a loop instead. Of course, computing
every element independently is not optimal and not necessary.
Considering just the fraction and ignoring the 1, we see
that this series can be computed recursively and cheaply by
adding a 2 and inverting it. We can then check the number
in the loop iteration by just adding an 1 and check its
fractional representation.

Whether the numerator has more digits than the denominator
or not can be checked cheaply by computing the log10, which
gives us the digit length minus one of the numerator. Raising
it to the power of 10, we get the smallest number with the
same digit length as the numerator. If the denominator is
smaller, it has less digits.
"""

from fractions import Fraction
from math import log10

def sol():
    # Loop counter and hit counter
    loop_cnt, hit_cnt = 0, 0

    # The fractional value
    frac = 0

    while loop_cnt <= 1000:

        # Compute k-th element
        loop_cnt += 1

        # Compute fraction
        frac = Fraction(1, 2 + frac)

        number = 1 + frac

        # Number of digits of numerator - 1
        l = int(log10(number.numerator))

        # If the denominator is smaller than the smallest (l+1)-digit number
        if 10**l > number.denominator:
            hit_cnt += 1
    
    return hit_cnt


print(sol())
