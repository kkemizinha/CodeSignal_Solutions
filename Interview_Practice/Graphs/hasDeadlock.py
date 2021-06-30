def hasDeadlock(connections):
    n = len(connections)
    visited = ['W'] * n
    for i in range(n):
        if visited[i] == 'W' and dfs(connections, i, visited):
            return True
    return False

def dfs(connections, s, visited):
    if visited[s] == 'G':
        return True
    if visited[s] == 'B':
        return False
    visited[s] = 'G'
    for v in connections[s]:
        if dfs(connections, v, visited) == True:
            return True
    visited[s] = 'B'
    return False