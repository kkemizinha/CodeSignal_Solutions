def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]
    for idx in range(len(inputArray) - 1):
       if ((inputArray[idx] * inputArray[idx+1]) > max):
           max = inputArray[idx] * inputArray[idx+1]
    return max