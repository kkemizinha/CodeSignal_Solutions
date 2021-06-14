# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 == None and l2 == None:
        return
    
    list_answer = ListNode(None)
    current = list_answer
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = ListNode(l1.value)
            l1 = l1.next
        else:
            current.next =  ListNode(l2.value)
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return list_answer.next