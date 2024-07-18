"""
The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in
some order, but it also has a rather interesting
sub-string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so
on. In this way, we note the following:

    d2 d3 d4  = 406 is divisible by 2
    d3 d4 d5  = 063 is divisible by 3
    d4 d5 d6  = 635 is divisible by 5
    d5 d6 d7  = 357 is divisible by 7
    d6 d7 d8  = 572 is divisible by 11
    d7 d8 d9  = 728 is divisible by 13
    d8 d9 d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with
this property.
"""

"""
For this problem, the brute-force method works, but I
remained very unsatisfied. For this way, we create all
permutations and check every substring whether it is
divisible by the corresponding prime or not. The problem
by using the 'itertools' permutation function is, that we
could check while permutating, if appending the next digit
gives us the necessary divisibility by the corresponding
prime number and if not, leave out all following permutations
with this digit at this position. And that's a lot!

So I wrote my own function which does exactly what I just
described. The method I used and adjusted is the Heap algorithm
for permutations, which is a smart and elegant recursive
algorithm. This way makes the code a little more complicated
but avoids computing a bunch of permutations which will be
thrown away anyway, after expensively computing the condition
for all of them.
"""

from itertools import permutations

def sol_brute_force(): 
    
    # Get all permutations from the itertools permutation function
    pandigitals = permutations("0123456789")

    # Divisors for the corresponding substrings
    DIVISORS = [2, 3, 5, 7, 11, 13, 17]
    sol = []

    for p in pandigitals:

        for i in range(7):

            # Get substring 
            substr = "".join(p[i+1:i+4])

            # If it is not divisible by the corresponding
            # prime, go to next pandigital
            if not int(substr) % DIVISORS[i] == 0:
                break
        else:
            # Break was never called. This pandigital
            # has the desired property
            sol.append(int("".join(p)))
            
    return sum(sol)


def sol_own_permutations():
    
    # Divisors for the corresponding substrings
    DIVISORS = [2, 3, 5, 7, 11, 13, 17]

    def perms(FinalPermList:list[str], PermString:str, ElementList:list[str]):
        """
        This recursive function creates permutations of the elements in
        the given list ElementList. Before appending the next element,
        it checks if this keeps the divisibility condition which is
        necessary for the problem.

        PermList: List where to store the permutations
        PermString: Current working string to add new elements
        ElementList: List of possible elements for add now
        """
        if len(ElementList) > 0:
            for e in ElementList:
                if not appending_keeps_divisibility(PermString, e):
                    continue
                NextPermString = PermString + e
                RemainingElements = ElementList.copy()
                RemainingElements.remove(e)
                perms(FinalPermList, NextPermString, RemainingElements)
        else:
            FinalPermList.append(int(PermString))
    
    def appending_keeps_divisibility(PString, e):
        """
        e is about to be appended. The number in question is
        the number starting from the second last digit in PString
        plus e, together 3 digits. The 0th divisor correspond to
        the number starting at the 1st index, 1st divisor to 2nd
        index and so on. Hence we need divisor at index start_inx-1
        """
        last_inx = len(PString)-1

        # Current string too short
        if last_inx < 2:
            return True

        # Append and check divisibility
        start_inx = last_inx-1
        return int(PString[-2:] + e) % DIVISORS[start_inx-1] == 0
        
        
    RESULT = list()
    perms(RESULT, "", list("0123456789"))
    
    return sum(RESULT)


print(sol_own_permutations())
