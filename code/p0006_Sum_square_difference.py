"""
The sum of squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the differnce between the sum of the squares of the
first one hundred natural numbers and the squares of the sum.
"""

"""
We can reduce the computation with appropriate formulas.

The square of the sum of n numbers is ( sum_{k=1}^n k )^2. The
inner sum is a Gauß sum, which has an explicit formula with n(n+1)/2.
This formula needs 3 operations in opposite to n-1 operations in
the expression as a sum.

The sum of squares of n numbers is sum_{k=1}^n k^2. This
computation needs 2n-1 operations. As above, this is a variant of
the Gauß sum and has an explicit formula with n(n+1)(2n+1)/6,
which needs 6 operations.

Combining these two, we accelerate the computation remarkably.
"""

def sol(n):
    return ( n * (n+1) / 2) ** 2 - (1/6) * n * (n+1) * (2*n+1)


# For comparison reasons, we compute the solutions this way too.
def explicit(n):
    # Square of the sum
    sqofsum = sum([i for i in range(1, n + 1)]) ** 2

    # Sum of the squares
    sumofsq = sum([i ** 2 for i in range(1, n + 1)])

    return sqofsum - sumofsq


print(sol(100))