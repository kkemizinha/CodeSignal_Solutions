# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if l is None:
        return
    if l.next is None:
        return l
    
    current = l
    total_nodes = 0
    while current is not None:
        total_nodes += 1
        current = current.next
    
    target_index_counter_previous = total_nodes - n
    if target_index_counter_previous <= 0:
        return l

    dummy = ListNode(-1)
    dummy.next = l
    current = l
    target = None
    last = None

    for i in range(1,total_nodes + 1):
        if i == target_index_counter_previous:
            target = current
        if i == total_nodes:
            last = current
        current = current.next
    
    last.next = dummy.next
    dummy.next = target.next
    target.next = None

    return dummy.next