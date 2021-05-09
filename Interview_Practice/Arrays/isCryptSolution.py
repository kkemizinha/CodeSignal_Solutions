from collections import defaultdict
def isCryptSolution(crypt, solution):
    sums = []
    for i in range(len(crypt)):
        sums.append(None)

    dict_letters = {}
    for i in range(len(solution)):
        dict_letters[solution[i][0]] =  solution[i][1]

    for i in range(len(crypt)):
        aux = ''
        for j in range(len(crypt[i])):
            aux += dict_letters[crypt[i][j]]
        sums[i] = aux
    
    if sums[0] == '0' and sums[1] == '0' and sums[2] == '0':
        return True
    if (int(sums[0]) + int(sums[1]) == int(sums[2])) and \
        (int(sums[0][0]) != 0  and int(sums[1][0]) != 0 and int(sums[2][0]) != 0):
        return True
    else:
        return False