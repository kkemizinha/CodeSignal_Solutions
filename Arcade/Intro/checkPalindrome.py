def checkPalindrome(inputString):
    if len(inputString) == 1:
        return True
    idx_start = 0
    idx_end = len(inputString) - 1
    while (idx_start < idx_end):
        if inputString[idx_start] == inputString[idx_end]:
            idx_start += 1
            idx_end -= 1
        else:
            return False
    return True