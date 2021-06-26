from collections import defaultdict
def groupingDishes(dishes):
    ingredients = defaultdict(list)
    for i in range(len(dishes)):
        for j in range(len(dishes[i])):
            if j != 0:
                ingredients[dishes[i][j]].append(dishes[i][0])

    for idx, el in enumerate(ingredients):
        ingredients[el].sort()

    answer_list = []
    for idx, el in enumerate(ingredients):
        if len(ingredients[el]) >= 2:
            aux = []
            aux.append(el)
            for j in range(len(ingredients[el])):
                aux.append(ingredients[el][j])
            answer_list.append(aux)

    answer_list.sort()

    return answer_list