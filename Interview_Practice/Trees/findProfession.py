def findProfession(level, pos):
    # Count the numbers of 1s in the
    # binary number that is related to
    # the index tree
    # For example. Level 3, pos 3
    # We will have node 6 (110)
    # We have 2 number '1's, so an even
    # number of 1 will return Doctor
    x = bin(pow(2,(level - 1)) + (pos - 1) ).count('1')
    return ['Doctor', 'Engineer'][x % 2]