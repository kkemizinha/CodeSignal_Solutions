def financialCrisis(roadRegister):
    # create another list taking off the row
    # and column
    answer = []
    size_roads = len(roadRegister)

    for i in range(size_roads):
        aux_append = []
        # Removing line i
        for j in range(size_roads):
            if i != j:
                aux_append.append(roadRegister[j][:i] + \
                                  roadRegister[j][i+1:])
        answer.append(aux_append)
    return answer