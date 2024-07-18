"""
The arithmetic sequence, 1487, 4817, 8147, in
which each of the terms increases by 3330, is
unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers
are permutations of one another.

There are no arithmetic sequences made up of
three 1-, 2-, or 3-digit primes, exhibiting
this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating
the three terms in this sequence?
"""

"""
We compute all 4-digit primes and check if this and
the two other numbers (+3330, +6660) are prime and
permutations of each other. 
"""
from useful_funcs import digit_list, get_primes_under

def sol():

    def are_permutations(a, b, c):
        return sorted(digit_list(a)) == sorted(digit_list(b)) == sorted(digit_list(c))

    # Get all 4-digit primes (sorted by default)
    four_digit_primes = [p for p in get_primes_under(10000) if p >= 1000]
    print([p for p in four_digit_primes if p <= 9999-2*3330])
    
    for p in four_digit_primes:

        # If b exceeds 9999, it is not 4-digit anymore
        if p > 9999-2*3330:
            break

        # Determine corresponding elements
        a = p+3330
        b = a+3330

        # If they are prime too and are permutations
        if (a in four_digit_primes and
            b in four_digit_primes and
            are_permutations(p, a, b) and
            p != 1487):
                
                return str(p)+str(a)+str(b)


print(sol())
