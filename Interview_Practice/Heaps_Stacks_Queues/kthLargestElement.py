import heapq
# The questions says to not use 
# built-in methods to access the
# kth element

def kthLargestElement(nums, k):
    nums = [-n for n in nums]
    # Transform into a heap
    # in-place
    heapq.heapify(nums)
    while k > 1:
        heapq.heappop(nums)
        k -= 1
    return -heapq.heappop(nums)