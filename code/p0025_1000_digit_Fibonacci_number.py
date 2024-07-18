"""
The Fibonacci sequence is defined by the recurrence relation:
    Fn = F_{n−1} + F_{n−2}, where F_1 = 1 and F_2 = 1.
Hence the first 12 terms will be:
    F_1 = 1
    F_2 = 1
    F_3 = 2
    F_4 = 3
    F_5 = 5
    F_6 = 8
    F_7 = 13
    F_8 = 21
    F_9 = 34
    F_10 = 55
    F_11 = 89
    F_12 = 144

The 12th term, F_12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?
"""

"""
Python is a very convenient programming language, as we do not
need to care about the length of integers. Python does that
for us, and the function sol() uses this fact by just computing
the index of the first 1000-digit number, no matter how big the
numbers become.
However, this problem seems to want the student writing a
function, which adds up large numbers and uses the addition
as we learned it in school digit by digit. This way is implemented
in sol2(). 
"""

from math import log10
from useful_funcs import digit_list

def sol():
    a = 1
    b = 1
    c = 2
    index_of_a = 1

    # If a has is less than 1000 digits
    # In Python, 1e+999 = inf, therefore we use log10
    while log10(a)+1 < 1000:
        a = b
        b = c
        c = a + b
        index_of_a += 1
    
    return index_of_a



def sol2():
    def add_together(a:list, b:list) -> list:

        # Current indices, which can be very different
        # when adding small with big numbers
        inx_a = len(a)-1
        inx_b = len(b)-1
        sol = list()

        # Carry number
        c = 0

        # While both numbers still have digits
        while inx_a >= 0 and inx_b >= 0:

            # Sum of both digits plus carry number
            tmp = a[inx_a] + b[inx_b] + c

            # Last digit of sum is the new digit of the new number
            sol.insert(0, tmp%10)

            # Keep further digits of carry number 
            c = tmp//10

            inx_a -= 1
            inx_b -= 1
        
        # Handle the remaining digits of a or b

        while inx_a >= 0:
            tmp = a[inx_a] + c
            sol.insert(0, tmp%10)
            c = tmp//10
            inx_a -= 1
        
        while inx_b >= 0:
            tmp = b[inx_b] + c
            sol.insert(0, tmp%10)
            c = tmp//10
            inx_b -= 1
        
        # Concatenate, if there are still digits carried
        return digit_list(c) + sol

    a = [1]
    b = [1]
    c = [2]
    index_of_a = 1

    while len(a) < 1000:
        a = b
        b = c
        c = add_together(a, b)
        index_of_a += 1
        
    return index_of_a


print(sol2())
