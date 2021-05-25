def allLongestStrings(inputArray):
    max = 0
    inputArraytoNum = []
    outputArray = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) > max:
            max = len(inputArray[i])
            inputArraytoNum.append(len(inputArray[i]))
    
    for j in range(len(inputArray)):
        if len(inputArray[j]) == max:
            outputArray.append(inputArray[j])
            
    return outputArray