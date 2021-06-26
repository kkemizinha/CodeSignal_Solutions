from collections import defaultdict

def containsCloseNums(nums, k):
    if nums is None:
        return False
    if len(nums) <= 1:
        return False
    if k == 0:
        return False

    dict = defaultdict(list)

    for idx, el in enumerate(nums):
        if el in dict and idx - dict[el] <= k:
            return True
        dict[el] = idx
    return False