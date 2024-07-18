"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers between 1 and 20?
"""

"""
The concept mentioned in the problem is known as least common multiple and we
want to compute lcm(1, ..., 20). An important property of this mapping is, that
it is associative, i.e. for some positive integers a_1, ..., a_n we have
lcm(a_1, ..., a_n) = lcm(lcm(a_1, ..., a_k), a_(k+1), ..., a_n) =
lcm(a_1, ..., a_k, lcm(a_(k+1), ..., a_n)).
Hence, we can use the result from the problem description and we have
lcm(1, ..., 20) = lcm(lcm(1, ..., 10), ..., 20) = lcm(11, ..., 20, 2520)

But how to compute this expression? A first approach is to check iteratively every
integer above or equal the biggest argument if it is divisibly by every a_i. The code is
short and elegant, but its computation is unsuitable expensive. For demonstration,
it is implemented below.

A better idea is this: We firstly compute all prime divisors for the a_i and consider
the factorization a = p_1 ^ l_1 * p_2 ^ l_2 * ... * p_k ^ l_k, where p_i is the
i-th prime number and l_i is the number of occurences in the factorization.
Now, for every prime number p_i, we find the biggest exponent occuring in the
factorizations of all a_i's called l'_i and we get the lcm by multiplying them:
lcm = p_1 ^ l'_1 * ... * p_k ^ l'_k.
Even if this way needs much more code, it is remarkable more efficient.

Proof: You can check very easily, that this must be the lcm. Obviously, every input a_i is
a divisor of lcm since every prime divisor in lcm occurs in the prime factorization
of a_i with exponents equal or smaller than those in lcm. On the other hand, if
there would be a smaller number as lcm, lets say lcm', at least one exponent in the
factorization of lcm' must be smaller than those of lcm. But then, there is one a_i
with a prime divisor with bigger exponent than lcm' and therefore a_i is not a
divisor of lcm'. Hence, lcm is minimal. □
"""

from useful_funcs import get_prime_divisors

def iterative_solution(lst):
    def is_common_multiple(candidate):
        # Check if all numbers in lst divides the candidate
        for i in lst:
            if not candidate % i == 0:
                return False
        return True

    # Start from the biggest number in lst as the first possible lcm
    m = max(lst)

    # Simply check for every number above iteratively, if it is a lcm
    while not is_common_multiple(m):
        m += 1

    return m


def sol(lst):

    # A list of tuples for (input_number, dict_of_prime_divisors)
    numbers_divisors_tuples = []

    # All prime numbers occuring in any input number as a divisor
    used_prime_numbers = set()

    for nmbr in lst:
        # Compute the prime divisors of this number
        divisors = get_prime_divisors(nmbr)

        # Save the number with the prime divisors as tuples
        numbers_divisors_tuples.append((nmbr, divisors))

        # Remember the used prime divisors in a set
        used_prime_numbers.update(divisors)

    # The lcm is now easy to calculate with the prime divisors as described above. We find
    # the biggest exponent for every prime divisor and multiply all prime numbers with the
    # biggest exponents together
    lcm = 1
    for p in used_prime_numbers:
        max_exponent = 0
        for (nmbr, divisors) in numbers_divisors_tuples:
            # If this number has p as a divisor, we take the exponent
            d = divisors.count(p)

            # Store the biggest exponent which occurs for this prime divisor
            max_exponent = max(max_exponent, d)

        # This prime divisor occurs as a factor in the lcm with the stored biggest exponent
        lcm *= p ** max_exponent

    return lcm


print(sol([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2520]))
