
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''
# Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node

'''
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.toNextMin(root)


    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return len(self.stack) > 0



    """
    @return: return next node
    """

    def _next(self):
        if len(self.stack) == 0:
            return None
        cur = self.stack.pop()      # pop out the most leftest node (smallest)
        self.toNextMin(cur.right)      # check if there is right node, which will be smaller than last value in stack
        return cur

    def toNextMin(self, root):
        while root:
            self.stack.append(root)
            root = root.left

