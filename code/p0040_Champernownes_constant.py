"""
An irrational decimal fraction is created by concatenating
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part
is 1.

If d_n represents the n-th digit of the fractional part,
find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

"""

"""
Just concenating the numbers and getting the indices is too
expensive. We need to store a number with 1000000 digits, that
is a number bigger than 10**100000. However, we can compute
the digits on the fly. We just increment the current number
and compute how many indices the number moves to the right.
"""

from useful_funcs import digit_list


def sol():
    # List of indices we consider
    desired_indices = [10**i for i in range(7)]

    # Number we are currently concatenating
    curr_nmb = 1

    # The digit list of the current number, helps us to determine exact index
    curr_nmb_list = [1]

    # Counts which index the first digit of the current number has reached
    index_counter = 1

    sol = []

    # While there are still numbers we need to find
    while len(desired_indices) > 0:

        # Move number list and counter
        last_nmb_list, last_counter = curr_nmb_list, index_counter

        # Create list of next number, its list and the next index
        curr_nmb += 1
        curr_nmb_list = digit_list(curr_nmb)
        index_counter += len(last_nmb_list)

        # If we exceed the desired index, the needed digit is in the last list
        if index_counter > desired_indices[0]:
            sol.append(last_nmb_list[desired_indices[0] - last_counter])
            del desired_indices[0]
    
    # Multiply the lists entries and return
    p = 1
    for i in sol:
        p *= i 
    return p
  
        
print(sol())
