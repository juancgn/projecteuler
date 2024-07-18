"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"""
We use a generator which gives us the next prime number. We request
and sum up all given prime numbers while they are below 2m. 
"""

from useful_funcs import prime_generator

def sol():
    # Generator must be instantiated
    prim_gen = prime_generator()

    sum_of_primes = 0
    curr_prime = 0

    # We add prime numbers as long as they are smaller than 2m.
    while curr_prime < int(2e6):
        # Add the prime number
        sum_of_primes += curr_prime

        # Request the next prime number
        curr_prime = next(prim_gen)

    return sum_of_primes


print(sol())
