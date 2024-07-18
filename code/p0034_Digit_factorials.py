"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

"""
The difficult part here is to find an upper bound. There must
be one as on the right hand side the biggest number we can
add by appending a digit is 9! = 362880. We need to approach
the upper bound in some way.
As 9! has 6 digits, we start with 6 digit numbers. The biggest
sum on the right hand side is 6 * 9! = 2177280, which has 7
digits. Computing 7 * 9! = 2540160, we see again 7 digits.
There is no 7 digits number above this, which is smaller than
its digit factorial sum and this is an upper bound for 6 digits.
If we append another digit, we just add at most 9! = 362880
on the right hand side, but on the left hand side we add even
for a 1 at least 10m. Every further digit adds up way more.
So our upper bound is 6 * 9! = 2177280, or rounded up at
2200000. 
"""

from useful_funcs import digit_list
from math import factorial as fac

def sol():

    sol = []

    # As 1! = 1 and 2! = 2, we start at 3
    n = 3
    while n < 2200000:

        # Create a list of the digits of n
        l = digit_list(n)

        # Check if n equals its digit factorials
        if n == sum( [fac(i) for i in l] ):
            sol.append(n)
            
        n+=1
    return sum(sol)


print(sol())
