"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""

import collections


class BSTIterator:  # BFS + level order
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.queue = collections.deque()
        self.nextmin(root)

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return self.queue

    """
    @return: return next node
    """

    def _next(self):
        if not self.hasNext:
            return None
        cur = self.queue.pop()  # cur == the moest left node, which is smallest
        self.nextmin(cur.right)  # check if the smallest node has smaller right node
        return cur

    def nextmin(self, root):
        while root:
            self.queue.append(root)
            root = root.left






