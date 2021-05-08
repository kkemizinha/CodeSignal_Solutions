def shapeArea(n):
    if (n == 0) or (n < 0):
        return 0
    if n == 1:
        return 1
    sum_value = 0
    for i in range(1,n):
        sum_value += i
    return (4*sum_value + 1)