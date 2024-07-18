"""
Take the number 192 and multiply it by each of 1, 2,
and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9
pandigital, 192384576. We will call 192384576 the
concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and
multiplying by 1, 2, 3, 4, and 5, giving the pandigital,
918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number
that can be formed as the concatenated product of an
integer with (1,2, ... , n) where n > 1?
"""

"""
To solve this problem, we firstly find every pandigital.
As we know that the numer 918273645 satisfies the condition,
we just need to concentrate on bigger numbers.
We sort the pandigitals in an descending order and loop
over them. For every p of them, we check for the first i digits,
i = 1, .., 4, if we can append the multiplies and somehow get
the pandigital. If we got one, we can return it.
"""
from itertools import permutations


MIN_NUM = 918273645

def sol():
    
    # Get permutations above MIN_NUM to get useful pandigitals
    perm_tuples = permutations(range(1, 9))
    pandigitals = list()
    for p in perm_tuples:
        
        # Convert tuple to number with leading 9
        num = 9 * 10**8 + sum( [p[i]*10**(len(p)-i-1) for i in range(len(p))] )

        # Smaller than the known pandigital number is not in consideration
        if num > MIN_NUM:
            pandigitals.append(num)
    
    # Sort the list of pandigital in a descending order
    pandigitals.sort(reverse=True)

    # Find the biggest pandigital which satisfies the condition
    for p in pandigitals:

        # The operations we need are most sutiable when using strings
        str_p = str(p)

        # Try multiplies of the first i digits... (more than 4 is not possible)
        for i in range(1, 5):
            
            # Get i digits of p
            starting_numb = str_p[0:i+1]
            tmp = ""

            # Append n*candidate as long as we are not too long
            n = 0
            while len(tmp) < len(str_p):
                n += 1
                tmp += str(int(starting_numb)*n)
            
            # If it fits, return it
            if tmp == str_p:
                return (p, int(starting_numb), n)


print(sol())
