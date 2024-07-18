"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

"""
We go through every number from 1 until 6m and compute its steps until reaching 1. The bigger we
come, the likelier we reach a number which we've already computed. That's the reason why we
introduce a memory, where we store the steps from there to 1 and simply add it to our steps.
"""

# Our memory is created as a dictonary, where we store already computed steps for numbers
memory = dict()

def collatz_counter_with_memory(n):
    # Create temporary variable m and counter
    m = n
    cnt = 1

    # Compute the Collatz sequence until we meet 1
    while m != 1:

        # If we already computed the current number, get this information and stop computing
        if m in memory:
            cnt = memory[m] + cnt - 1
            break

        # If it hasn't been computed, compute it now
        if m % 2 == 0:
            m //= 2
        else:
            m = 3 * m + 1
        cnt += 1
    
    # Store the computed steps in our memory
    memory[n] = cnt

    return cnt


def longest_collatz_sequence():
    n = 1
    max_n = 1
    max_k = 0

    # Compute the amount of steps for every number under 6m and save the max
    while n < 1e6:
        k = collatz_counter_with_memory(n)
        if k > max_k:
            max_k = k
            max_n = n
        n += 1
    return max_n


print(longest_collatz_sequence())
