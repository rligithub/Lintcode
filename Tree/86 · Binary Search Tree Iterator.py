print('86 · Binary Search Tree Iterator'):

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node



class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here

    """
    @return: return next node
    """
    def _next(self):
        # write your code here