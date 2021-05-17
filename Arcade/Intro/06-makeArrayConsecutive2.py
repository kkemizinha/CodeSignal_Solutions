def makeArrayConsecutive2(statues):

    if len(statues) == 0 or len(statues) == 1:
        return 0 
    statues.sort()
    intervalValues = statues[-1] - statues[0] + 1
    diff = intervalValues - len(statues)
    return diff