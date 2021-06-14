# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# Supposing both lists are not sorted

def mergeTwoLinkedLists(l1, l2):
    if l1 == None and l2 == None:
        return
    
    list_to_be_sorted = []
    
    #concatenate both lists
    #apply sort
    def getValuedLinkedList(l1_aux, list_to_be_sorted):
        current = l1_aux
        while current != None:
            list_to_be_sorted.append(current.value)
            current = current.next
        return list_to_be_sorted
    
    if l1 is not None:
        list_to_be_sorted = getValuedLinkedList(l1, list_to_be_sorted)
    if l2 is not None:
        list_to_be_sorted = getValuedLinkedList(l2, list_to_be_sorted)
    list_to_be_sorted.sort()
    
    current = l1
    if l1 is None:
        current = l2
    
    for idx, val in enumerate(list_to_be_sorted): 
        if current is not None and current.next is not None:
            current.value = val
        elif current is not None and current.next is None:
            current.value = val
            if idx + 1 < len(list_to_be_sorted):
               current.next = ListNode(list_to_be_sorted[idx + 1])
        elif current is None:
               current = ListNode(val)
        current = current.next
        
    if l1 is None:
        return l2

    return l1
