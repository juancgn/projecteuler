"""
Euler discovered the remarkable qudratic formula:
n**2 + n + 41.

It turns out that the formula will produce 40 primes for the
consecutive integer values 0 <= n <= 39. However, when n=40,
40**2 + 40 + 41 = 40*(40+1) + 41 is divisible by 41, and
certainly when n=41, 41**2 + 41 + 41 is clearly divisibly by
41.

The incredible formula n**2 - 79n + 1601 was discovered, which
produces 80 primes for the consecutive values 0 <= n <= 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n**2 + an + b,
where |a| < 1000 and |b| <= 1000,
where |n| is the modulus/absolute value of n,
e.g. |11| = 11 and |-4| = 4.

Find the product of the coefficients, a and b, for the
quadratic expression that produces the maximum number of
primes for consecutive values of n, starting with n=0.
"""

"""
We try for every possible combination of 'a' and 'b', how
long the sequence of primes those pairs provide. Since we
start at n=0, and therefore f(0) must be prime, we must
restrict b to prime numbers (positive!).
Furthermore, since the problem description provides an
example with 39 primes in a row, we do not need compute the
sequence, if f(39) is not prime.
"""
from useful_funcs import is_prime


def sol():

    def f(a, b, n):
        return n*n + a*n + b

    # Create a list of possible numbers for 'a' (every number with |a| < 1000)
    complete_list = list(range(-999, 1000))

    # Create a list for the 'b's, which must be prime or the negative equivalent
    prime_list = [b for b in complete_list if is_prime(b)]

    max_length = 0
    max_pair = ()

    # Loop over possible b's and compute for every 'a' the sequence length
    for b in prime_list:
        for a in complete_list:

            # We know that (1, 41) in the description already has 39 primes
            if not is_prime(f(a, b, 39)):
                continue

            # Compute the prime sequences length
            n = 0
            while is_prime(f(a, b, n)):
                n += 1
            
            # Find the maximum
            if n > max_length:
                max_length = n
                max_pair = (a, b)
    
    # Return the product of 'a' and 'b' of the pair with the longest sequence
    return max_pair[0]*max_pair[1]


print(sol())
