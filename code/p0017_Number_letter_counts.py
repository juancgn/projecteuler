"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use
of "and" when writing out numbers is in compliance with British usage.
"""

"""
We create a dict with the string representation of every number up to 1000.
Then, we count the lengths of those strings and sum them up.
"""

# Define special numbers
lst = {1: 'one',
       2: 'two',
       3: 'three',
       4: 'four',
       5: 'five',
       6: 'six',
       7: 'seven',
       8: 'eight',
       9: 'nine',
       10: 'ten',
       11: 'eleven',
       12: 'twelve',
       13: 'thirteen',
       14: 'fourteen',
       15: 'fifteen',
       16: 'sixteen',
       17: 'seventeen',
       18: 'eighteen',
       19: 'nineteen',
       20: 'twenty',
       30: 'thirty',
       40: 'forty',
       50: 'fifty',
       60: 'sixty',
       70: 'seventy',
       80: 'eighty',
       90: 'ninety'}

def get_written_number(nmbr:int):

    # If this number is already handled, return
    if nmbr in lst:
        return lst[nmbr]
    
    # Numbers under 100 can be written by just concatenate tens and ones
    if nmbr < 100:
        return lst[(nmbr // 10) * 10] + ' ' + lst[nmbr % 10]

    # Numbers between 100 and 999 can be written by "... hundred and ..." or "... hundred"
    elif nmbr < 1000:

        # We need to access lower entries in the dict. Although we expect this function
        # to be called in a ascending order, we protect us from unexpected behaviour by
        # using a try and except environment
        try:

            # If the number is a multiple of 100, its string is just '... hundred'
            if nmbr % 100 == 0:
                return lst[nmbr // 100] + ' hundred'
            
            # Otherwise, we need to concatenate "... and ..."
            else:
                return lst[nmbr // 100] + ' hundred and ' + lst[nmbr % 100]
            
        except:
            print(f"{nmbr//100} or {nmbr % 100} is not considered yet")
    
    elif nmbr == 1000:
        return 'one thousand'


def count_letters():

    # Get the strings for the numbers 21 to 1000
    for nmbr in range(21, 1001):
        lst[nmbr] = get_written_number(nmbr)
    
    # Sum up the string lengths without spaces
    s = 0
    for nmbr in lst:
        s += len( lst[nmbr].replace(' ', '') )
    
    return s


print(count_letters())
