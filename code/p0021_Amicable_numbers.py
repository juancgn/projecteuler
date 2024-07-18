"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and
110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

"""
We check every number bigger than 1 and smaller than 10000. Since an amicable pair
must be a pair of an abundant and a deficient number (otherwise a=b), we can only
consider abundant numbers.
"""
from useful_funcs import get_all_divisors


def amicable_numbers():
    amicable_nums = set()
    p = 2
    while p < 1e+4:
        # Get all proper divisors
        div_p = get_all_divisors(p).difference({p})

        # Compute the sum of those divisors
        q = sum(div_p)

        # If the sum q is smaller than p, we already considered q
        if p < q:
            if sum(get_all_divisors(q).difference({q})) == p:
                amicable_nums.update((p, q))

        p += 1

    return sum(amicable_nums)


print(amicable_numbers())
