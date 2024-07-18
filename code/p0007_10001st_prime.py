"""
By listing the first six prime numbers:
2, 3, 5, 7, 11 and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""
We can solve it just by checking every odd number if it is prime and
counting the prime numbers on the way until we found the n-th one.
"""

from useful_funcs import is_prime

def prime_number_by_index(n):
    # The second (counter=2) prime number is 3. p stores the current prime number.
    # By starting with p=3, we can add 2 every iteration because from now on, every prime number is odd.
    counter = 2
    p = 3
    while not counter == n:
        # Next possible prime number is the next odd number
        p += 2

        # If it is prime, increment the counter.
        if is_prime(p):
            counter += 1

    return p


print(prime_number_by_index(10001))
