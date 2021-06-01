# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    if l == None:
        return l
    elif l.value == k:
        l = l.next
    
    current = l
    
    while current != None and current.next != None:
        if current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
    
    if current is not None and current.value == k:
        l = []
    
    return l