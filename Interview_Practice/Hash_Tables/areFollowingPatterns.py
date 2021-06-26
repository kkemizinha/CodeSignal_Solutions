from collections import defaultdict

def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False

    elements_total = defaultdict(list)

    for elstring, elpatterns in zip(strings, patterns):
        if elpatterns not in elements_total[elstring]:
            elements_total[elstring].append(elpatterns)
            if len(elements_total[elstring]) > 1:
                return False
    if len(elements_total) != len(set(elements_total.values())):
        return False

    return True
