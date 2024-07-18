"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

"""
The straightforward solution is very fast.
"""
from useful_funcs import is_prime

number = 600851475143

def sol(numb):
    # p is the current prime divisor. It will only be updated, if a division is not possible.
    # Otherwise, there could be more divisions by p possible, hence no update needed.
    p = 2

    # We divide by the prime divisors until we get a 1.
    while not numb == 1:

        # Find next prime number
        while not is_prime(p):
            p += 1

        # If we have a prime divisor, we divide numb by p as many times as possible.
        while numb % p == 0:
            numb = numb // p
        p += 1

    return p-1


print(sol(number))
