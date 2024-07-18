"""
The nth term of the sequence of triangle numbers is given
by, tn = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form
a word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t_10. If the word value is a triangle number
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English
words, how many are triangle words?
"""


"""
The challenge is to find a way to know, whether a specific
number (in this case the 'word value' of a word) is a triangle
number or not. All triangle numbers have the form n(n+1)/2, so
if there is a integer n which is mapped to the word value by this
function, the world value is a triangle number. We just reverse
the function to n = +sqrt(2t - 1/4) - 1/2 and if this is a int
(n % 1 == 0), the number is a triangle number.
"""

import string
from math import sqrt

def sol():
    def word_value(word):
        # Get the position + 1 of every character in the standard string ABCD...
        return sum( [string.ascii_uppercase.index(c)+1 for c in word] )
    
    def is_triangle(t):
        # Inverse function of n(n+1)/2
        n = sqrt(2*t + 0.25) - 0.5

        # Return whether n is integer or not
        return n % 1 == 0

    # Get words
    with open('resources/p042_words.txt') as f:
        words = f.read().replace('\"', '').split(',')
    
    # Loop over all words and count how many have a triangle word value
    counter = 0
    for w in words:
        counter += is_triangle(word_value(w))

    return counter


print(sol())
