def firstDuplicate(a):
    seen = set()
    for i in range(len(a)):
        if a[i] not in seen:
           seen.add(a[i])
        else:
            return a[i]
    return -1