"""
It was proposed by Christian Goldbach that
every odd composite number can be written as
the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be
written as the sum of a prime and twice a square?
"""

"""
We assume the number we are looking for is below
10000, otherwise we choose a bigger upper bound.
We get all primes under 10000 (with a sieve).
We check numbers n starting from 9 and loop over
all primes under n, if one of them fits, meaning
if the number which doubled square added to this
prime gives us n is an integer. If there is one,
this number is an odd composite which surely can
be written as the sum of a prime and twice a
square. If not, we found the desired smallest one.
"""

from useful_funcs import get_primes_under
from math import sqrt

def sol():
    primes = get_primes_under(10000)
    
    # Helps us to point to the smallest prime above n
    ptr = 0

    n = 9

    while True:

        # We consider odd composites, hence no primes
        if n not in primes:

            # Move the pointer
            while primes[ptr] < n:
                ptr += 1
            
            primes_until_pointer = primes[:ptr]

            # Loop over the primes under n and check
            # if a set of suitable numbers exists
            set_of_numbs_exist = False
            for p in primes_until_pointer:
                if sqrt((n-p)/2) % 1 == 0:
                    set_of_numbs_exist = True
                    break
            if not set_of_numbs_exist:
                return n

        n += 2


print(sol())
