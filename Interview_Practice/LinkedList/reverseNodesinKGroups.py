# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    if k <= 1:
        return l
    if k is None:
        return
    if l.next is None:
        return

    # This function will reverse the sublist
    # with k elements. I will use 5 pointers.
    # Supposing l is and k = 3:
    #   [1]->[2]->[3]->[4]->[5]->[6]
    # The first call will be:
    #   [dummy]->[1]->[2]->[3]->[4]
    # We have sent extra elements to this 
    # function because the first element
    # can point to the next sublist. 
    # Eg: [1] -> [4] in the end.
    # It returns:
    #  [3]->[2]->[1]->[4]
    def reverse(start, end):
        # stores the beginning of the sublist
        previous = start.next
        current = previous.next
        while current != end:
            next_node = current.next
            current.next = start.next
            start.next = current
            current = next_node
        previous.next = end
        return previous

    # dummy node will help
    # with previous ptr
    dummy = ListNode(-1)
    dummy.next = l
    
    count = 0

    # point the previous
    # node before the start
    # node list
    previous = dummy
    current = l

    while current != None:
        count += 1
        # I will send sublists. eg [1-3], [4-6]
        if count % k == 0:
            previous = reverse(previous, current.next)
            current = previous.next
        else:
            current = current.next
    return dummy.next