#Solved in: 5 min
def alphabeticShift(inputString):
    output = ""
    for el in inputString:
        if ord(el) + 1 <= ord('z'):
            output += chr(ord(el) + 1)
        else:
            output += 'a'
    return output