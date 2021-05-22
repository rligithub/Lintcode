print('95 · Validate Binary Search Tree')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):

        return self.helper(root,float('inf'), float('-inf'))

    def helper(self,root,Max,Min):

        if not root:
            return True

        if root.val <= Min or root.val >= Max:
            return False

        isBST_left = self.helper(root.left,root.val,Min)
        isBST_right = self.helper(root.right,Max,root.val)

        return isBST_left and isBST_right












root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)

a=Solution()
print(a.isValidBST(root))
