def roadsBuilding(cities, roads):

    # Create a graph representation using a dict
    # 0: 1
    # 1: 0, 2
    # 2: 1
    
    # For each node, check if all nodes were there
    # with the help of a for loop..
    # If not available, add to the output set
    # Because sets do not allow duplicate entries
    # How to eliminate the repetition in output?
    # 1a. Order each pair in crescent order all the pairs
    # 2. set will do its work
    # 0: 3
    # 1: 3
    # 2: 3
    # 3: 1, 2, 3
    
    # Transform set into list
    
    graph = {}
    def add_edges(graph_aux, el, value):
        if el not in graph_aux:
            graph_aux[el] = [value]
        else:
            graph_aux[el].append(value)
        return graph_aux

    for i in range(0,len(roads)):
        graph = add_edges(graph, roads[i][0], roads[i][1] )
        graph = add_edges(graph, roads[i][1], roads[i][0] )
    
    output = set()
    for i in range(0, cities):
        for j in range(0, cities -1):
            if i != j:
                if i not in graph:
                        pair = tuple(sorted([i,j]))
                        output.add(pair)
                else:
                    if j not in graph[i]:
                        pair = tuple(sorted([i,j]))
                        output.add(pair)

    output = sorted(output)
    output = list(output)

    return output