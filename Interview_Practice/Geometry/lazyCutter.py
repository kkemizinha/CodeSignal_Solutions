def lazyCutter(n):
    # Supposing n = 3
    # We can cut in traversal which
    # give us an extra slice. Then,
    # with this info we add +1. E.g:
    #  1+ 3 + (3-1) + (3-2) + (3-3) = 7
    if n == 0:
        return 0
    return int(1 + n*(n+1)/2)