"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

"""
We create a list of the names from the file, sorting them in an ascending order and enumerate them
with their index. Then, we loop over that and sum up the scores.
"""
import string


def names_scores():
    def score(index, name):

        # Sum up the alphabetical values of the name
        s = 0

        for char in name:
            
            # Add the incremented index of the character from the ascii list ("ABCD...XYZ")
            s += string.ascii_uppercase.index(char) + 1
        
        # Return the score provided by the product of index and alphabetical score
        return s * index

    with open("resources/p022_names.txt") as f:
        # Create a list from the file by removing the quotation marks and seperate the names by the comma
        names = f.read().replace('\"', '').split(',')

    # Sort the list by a ascending order
    names.sort()

    # Create a list of tuples with the name and its index in the list (inx, name), starting from index 1
    names = enumerate(names, 1)

    # Sum up the scores
    score_sum = 0

    for (inx, name) in names:

        score_sum += score(inx, name)

    return score_sum


print(names_scores())
