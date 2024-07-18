"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series,
1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

"""
We compute it with an one-liner thanks to Python.
Computing it explicitly is very fast.
"""

def sol():
    # Compute the self powers and sum them up
    return sum([n**n for n in range(1, 1001)])%(10**10)


print(sol())
