"""
Starting with the number 1 and moving to the right in a
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the
diagonals is 101.

What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral formed in the same way?
"""

"""
There are multiple ways to solve this problem. The 'easy' way
is to let the program create a 2D array as in the problem
description and sum up the diagonal elements. For this, we
create a 2D array filled with zeros and assign 1 to the
centered cell (Note that the size of the array must be odd
to ensure there are centered row and column). Then, we start
with the element to the right (j+1) and start a nested while
loop.

The outer while loop, which runs as long as i and j are not
out of range, contains four while loops representing the
four ways down, left, up, right. We go down, as long as
the element to the left is not zero (i. e. does exist).
Then, we go left, as long as the element above is not zero
and so on. On our way, we fill the cells with the natural
numbers.

After we filled the array, we can sum up the diagonal
elements with one loop very easily. Note that we needed to
fill the whole field but do only need the diagonal elements
and this is not efficient.

However, after thinking about this problem, we may recognize
that there is a way to describe the diagonal elements with a
formula. On every layer, the four elements at the corners
differ by a multiply of 2. At the first layer its 2, the
second layer 4, the third layer 6 and so on. Imagining the
diagonal elements in an ascending order, the sequence can
be described as

d(0) = 1,
d(n) = d(n-1) + 2 * ((n-1) // 4) + 2,

where "//" is an integer division. As an object with size
N has 2*(N-1) diagonal elements (excluding the center), our
solution is the sum of d(0), ..., d(2*(N-1)).
"""

def sol():
    SIZE = 1001

    # Create field and fill with zeros
    field = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    
    # Start with the cell in center and go right
    i = j = SIZE//2
    field[i][j] = 1
    j += 1
    n = 2

    # While we still have empty fields
    while i < SIZE and j < SIZE:
        # down
        while i < SIZE and field[i][j-1] != 0:
            field[i][j] = n
            n += 1
            i += 1

        # left
        while j >= 0 and field[i-1][j] != 0:
            field[i][j] = n
            n += 1
            j -= 1

        # up
        while i >= 0 and field[i][j+1] != 0:
            field[i][j] = n
            n += 1
            i -= 1

        # right
        while j < SIZE and field[i+1][j] != 0:
            field[i][j] = n
            n += 1
            j += 1

    # Sum up diagonal entries
    s = 0
    for k in range(SIZE):
        s = s + field[k][k] + field[SIZE-k-1][k]

    return s-1

def sol2():
    SIZE = 1001

    # Store the diagonal elements in a list
    l = list()
    l.append(1)

    # Compute all diagonal elements (there are 2*(SIZE-1) elements excluding 1)
    for i in range(1, 2*(SIZE-1)+1):
        l.append(l[i-1] +  2*((i-1)//4) + 2 )
    
    # Sum up and return
    return sum(l)

def print2DField(field):
    result = ""
    for p in field:
        s = "["
        for k in p:
            if k < 10:
                s = s + f"   {k}"
            elif k < 100:
                s = s + f"  {k}"
            else:
                s = s + f" {k}"
        s = s + " ]"
        result = result + s + "\n"
    print(result)


print(sol())
