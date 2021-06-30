#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def traverseTree(t):
#BFS
    if t is None:
        return []
    solution = []
    queue = []
    queue.append(t)
    
    while (len(queue) > 0):
        
        node = queue.pop(0)
        solution.append(node.value)
        
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
    
    return solution