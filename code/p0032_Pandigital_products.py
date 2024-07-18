"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through
9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be
sure to only include it once in your sum.
"""

"""
We solve this problem by checking for every possible product whether
there is a pair of multiplicand and multiplier, which satisfy the
condition, or not. Note that we only need to check products with 4
digits. The reason is that products with 5 or more digits leave 4
or less digits for the multiplicand and multiplier. But every
possible combinations leads to a product with 4 digits or less:
9 * 999 = 8991
99 * 99 = 9801
We use a loop to check every candidate. First, we sort out numbers
which contains zeros. Then, we sort out numbers which contains
duplicates. If a number passes those checks, we determine its
divisors, create tuples of multiplicand / multiplier for this number
and check for every pair, whether they use exactly the remaining
digits, which are not used in the product, or not.
"""
from useful_funcs import digit_list, get_all_divisors

def sol():
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # We only check numbers with four digits
    threshold = 9999

    found = set()

    for n in range(1, threshold+1):

        # If n has a zero, it does not satisfy the condition
        n_list = digit_list(n)
        if 0 in n_list:
            continue

        # If n has duplicates
        if len([d for d in n_list if n_list.count(d) > 1]) > 0:
            continue
        
        # Get tuple divisors (n = sqrt(n)*sqrt(n) is not pandigital)
        div = {(d, n//d) for d in get_all_divisors(n) if d*d < n}

        # Get the digits not used in n
        remaining_digits = digits.difference(n_list)

        # Check for every divisor tuple ...
        for (a, b) in div:

            # Get list of digits of a and b
            div = digit_list(a) + digit_list(b)

            # If there are duplicates, leave
            if len([d for d in div if div.count(d) > 1]) != 0:
                continue

            # If their digits fits to the remaining digits, we found a number
            if set(div) == remaining_digits:
                found.add(n)

    return sum(found)


print(sol())
