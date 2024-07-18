"""
You are given the following information, but you may prefer
to do some research for yourself.

    - 1 Jan 1900 was a Monday.
    - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

"""
We create a list, where every cell represents a day in the
relevant period (except first cell, to start with 1) and
contains the order this day has in its month. So, the list
looks like this:
[None, 1, 2, ..., 30, 31, 1, 2, ..., 27, 28, 1, 2, ...]
and so on. The extra day in leap year needs to be included!
We loop over every year and determine the proper list of
days depending on the month and the year, before we extend
our list with this list.

After creating the list, we check every cell if it satisfies
the following condition:
1. The cell contains a 1, meaning it is the first day in the
month
2. The index of the cell satisfies the condition (i+1) % 7 == 0,
meaning that this day is a Sunday. As the first day starts on
a Monday, the + 1 is necessary, because this Monday is the
second day in the 7-days-periods of Sundays.

Counting the cells which satisfy the conditions, we
get the desired result.
"""


def sol():
    def is_leap_year(year):
        return (year % 4 == 0) and ( (not year%100==0) or year%400==0)
    
    # Standard month lengths
    std_month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   

    # List of all days and their order in their month, starting at 1
    day_of_month = [None,]

    # Loop over every year
    for y in range(1901, 2000 + 1):

        # Get the lengths of the months and adjust if necessary
        month_lengths = std_month_lengths.copy()
        if is_leap_year(y):
            month_lengths[1] = 29

        # Extend our list by a list of the days in every month
        for m_length in month_lengths:
            day_of_month.extend(list(range(1, m_length+1)))
    
    # Go through the list and count the cells satisfying the conditions
    cnt = 0
    for i in range(1, len(day_of_month) + 1):

        # If the day is a Sunday and it is the first in the month
        # Since we start on a Monday, we add 1
        if (i+1) % 7 == 0 and day_of_month[i] == 1:
            cnt += 1
    
    return cnt


print(sol())
