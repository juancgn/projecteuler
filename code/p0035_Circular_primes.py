"""
The number, 197, is called a circular prime because
all rotations of the digits: 197, 971, and 719, are
themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

"""
For every number below 1m, we check if it is prime and
its rotations are prime.
"""
from useful_funcs import digit_list, is_prime

def sol():
    def list_to_int(t):
        return sum( [t[-i-1] * 10**i for i in range(len(t))] )

    def rotations(n):
        rotats = []
        n_list = digit_list(n)

        # There are as many rotations as digits of n (excluding n)
        k = len(n_list) - 1
        while k > 0:

            # Append the first digit to the end
            n_list.append(n_list[0])

            # Delete the first digit
            del n_list[0]

            rotats.append(list_to_int(n_list))
            k -= 1

        return rotats

    counter = 0

    # Check the rotations for every number under 1m
    n = 1
    while n < 1e+6:

        # If n is not prime, we can continue
        if is_prime(n):
            rots = rotations(n)

            # Check all rotations if they are prime
            all_prime = True
            for rot in rots:
                if not is_prime(rot):
                    all_prime = False
                    break
            if all_prime:
                counter += 1

        n += 1
    return counter


print(sol())
