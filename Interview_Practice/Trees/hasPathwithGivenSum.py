#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if t is None:
        return False
    else:
        #subtract from current node
        answer = False
        aux_sum = s - t.value

        # Subtract from s until == 0
        # Test if we are on already on final leaf
        if ((aux_sum == 0) and (t.left is None) \
             and (t.right is None)):
             return True
        
        if t.left is not None:
            answer = answer or hasPathWithGivenSum(t.left,aux_sum)
        if t.right is not None:
            answer = answer or hasPathWithGivenSum(t.right,aux_sum)
        
        return answer