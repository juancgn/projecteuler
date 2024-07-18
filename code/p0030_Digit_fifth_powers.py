"""
Surprisingly there are only three numbers that can be
written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as
the sum of fifth powers of their digits.
"""

"""
The biggest step to take for this problem is to find
an upper bound. As we can easily see, there must be an
upper bound, because the biggest number we can add on
the right hand side is 9^5 = 59049, but if the number
on the left hand side gets too big, every digit we append
has an effect to the sum surely greater than 9^5. A 5
digit number can have the maximum fifth digit power sum
of 5 * 9^5 = 295245. This is bigger than every 5 digit
number. For a 6 digit number its 6 * 9^5 = 354294. That
means, there is no 6 digit number above this whose fifth
digit power sum is bigger than the number. If we append
a digit, this digit produces an addition of at least
1 million, which surely exceeds 9^5. Therefore, 354294,
rounded up to 400000, is an upper bound.
"""

from useful_funcs import digit_list

def sol(): 

    sol = []
    for n in range(2, 400000):
        
        # Get list of the digits of n
        l = digit_list(n)

        # If n equals its fifth digit powers
        if n == sum( [i**5 for i in l] ):
            sol.append(n)
            
    return sum(sol)


print(sol())
