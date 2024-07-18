"""
In the United Kingdom the currency is made up of pound (£)
and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number
of coins?
"""

"""
This is a wonderful problem to use a recursion. A recursion
step receives a sorted list with used coins (with multiples) and
loop over next possible coins. It also receives a index pointer
indicating which index the coin we recently added has in the ALL_COINS
list. This helps us not only to continue with the correct next coin
but also let us easily access the remaining coins we can use from the
ALL_COINS list with a short statement in the loop header.
Note that this means that we cannot append any coin in a specific step
but only the same or the next smaller one. This avoids multiple tuples
of the same coins in a different order.
"""


def sol():
    ALL_COINS = [200, 100, 50, 20, 10, 5, 2, 1]

    # We store the results outside the recursion (makes it easier)
    RESULTS = []

    def coin_sums(coins, curr_inx):
        s = sum(coins)

        # No more coins possible
        if s >= 200:

            # If we found a proper coin set
            if s == 200:
                RESULTS.append(tuple(coins))
            return

        # Loop over the remaining coins (including the current) and
        # add them to the coin list 
        for i in range(curr_inx, 8):
            coin_sums(coins + [ALL_COINS[i]], i)
        
    coin_sums([], 0)
    return len(RESULTS)


print(sol())
