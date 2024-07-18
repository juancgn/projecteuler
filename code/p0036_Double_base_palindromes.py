"""
The decimal number, 585 = 10010010012 (binary), is
palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either
base, may not include leading zeros.)
"""

"""
We construct palindromes (base 10) by the following method: If we want
palindromes of an odd length, take every number of the numbers of half the
length (round up), reverse the digit order (ignore the last digit)
and append it to this number. If we want an even length, reverse the digit
order of numbers with half the length and append this to them. Note that
palindromes of length 2k-1 and 2k use the same set of numbers of half the
length because rounding (2k-1)/2 is equals to 2k/2. Hence, we start with
an odd number (k=1) and every time we compute even palindromes, we use the
list of numbers half-the-length from the last loop.
"""
from useful_funcs import  is_palindrome

def sol():
    def bin_to_dec(bin):
        return int(str(bin), 2)
    def dec_to_bin(dec):
        return bin(dec)[2:]

    max_digits = 6
    palindromes = []
    tmp = []

    # Find palindromes for every length until max_digits
    for k in range(1, max_digits+1):

        if k % 2 == 1:
            # Get all numbers with half the length, rounded up.
            tmp = range(10**(k//2), 10**(k//2 + 1))

            # Create palindromes of length k by reversing the digit order
            # and appending it to the number while ignoring the last digit
            k_pals = [int(str(d) + str(d)[::-1][1:]) for d in tmp]
        else:

            # From the last loop, tmp all numbers exactly the length of k/2
            # Create new palindromes by appending the number in a reversed
            # order of digits to the number
            k_pals = [int(str(d) + str(d)[::-1]) for d in tmp]

        palindromes.extend(k_pals)
    
    # Return the sum of all the palindromes which are palindromic in their
    # base-2-representation
    return sum( [pal for pal in palindromes if is_palindrome(int(dec_to_bin(pal)))] )


print(sol())
