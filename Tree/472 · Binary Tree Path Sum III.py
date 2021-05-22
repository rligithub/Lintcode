print('472 · Binary Tree Path Sum III')


class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):


root = ParentTreeNode(1)
root.left = ParentTreeNode(2)
root.right = ParentTreeNode(3)
root.right.left = ParentTreeNode(2)
root.left.left = ParentTreeNode(4)
target = 6

a = Solution()
print(a.binaryTreePathSum3(root, target))