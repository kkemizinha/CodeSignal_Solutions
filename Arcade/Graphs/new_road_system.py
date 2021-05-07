def newRoadSystem(roadRegister):
    # Verify if number of connections are even
    # O(n)
    for i in range(len(roadRegister)):
        count = 0
        for j in range(len(roadRegister)):
            if roadRegister[i][j] == True:
                count += 1
            if roadRegister[j][i] == True:
                count -= 1
        if count != 0:
            return False

    return True
