def climbingStairs(n):
    a = 1
    b = 0
    for _ in range(n):
        a, b = a + b, a
    return a