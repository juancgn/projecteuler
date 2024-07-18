"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

"""
We check every odd number n above 10 if it is truncatable or not.
After checking the prime property for n itself, the truncatable
check itself happens with two loops, where the first loop removes
digit by digit from the left side and check if it is prime. This
happens by dividing the number by the biggest power of 10 below n.
The second loop removes digit by digit from the right, which can
easily implemented by just using an integer divison by 10, and then
checks the prime property.

Unfortunately, we do not know a upper bound for n. But since the
question provides the amount of truncatable numbers, we simply
check if we found all 11 yet in the loop condition.
"""
from useful_funcs import is_prime
from math import log10

def sol():
    def is_truncatable(p):
        if not is_prime(p):
            return False

        ### Remove from left
        
        # Biggest power of 10 below p
        i = int(log10(p))

        numb = p

        # Remove first digit and check prim property as
        # as long as there is more than one digit (was
        # checked in last loop)
        while numb >= 10:
            # Remove first digit
            numb = numb - (10**i) * (numb//(10**i))

            if not is_prime(numb):
                return False

            # The biggest power of 10 below numb is now
            # exactly one smaller
            i -= 1
        
        ### Remove from right
        
        numb = p
        # Remove last digit and check prim property
        while numb >= 10:
            # Remove last digit
            numb = numb // 10

            if not is_prime(numb):
                return False
        
        # All are prime
        return True
            
    # Check odd numbers above 10
    sol = list()
    n = 11
    while len(sol) < 11:
        if is_truncatable(n):
            sol.append(n)
        
        n += 2

    return sum(sol)


print(sol())
