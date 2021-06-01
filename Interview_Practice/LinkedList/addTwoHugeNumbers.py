# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
 
def addTwoHugeNumbers(a, b):

    def read_list(list_read):
        number_str = ''
        current = list_read
        while current != None:
            zerosleft = 4 - len(str(current.value))
            number = zerosleft * '0' + str(current.value)
            number_str += number
            current = current.next
        return number_str
    
    sum = 0
    sum = str(int(read_list(a)) + int(read_list(b)))
    
    n = len(sum)
    output = []
    
    for i in range(n, 0, -4):
        el = ''
        if i - 4 >= 0:
            el = sum[i - 4:i]
        else:
            el = sum[0:i]
        output.insert(0,int(el))

    return output