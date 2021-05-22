print('97 · Maximum Depth of Binary Tree')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    # recursion function
    def maxDepth3(self, root):
        if not root:
            return 0

        left = self.maxDepth3(root.left)
        right = self.maxDepth3(root.right)

        return 1 + max(left, right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(5)
root.right.left.left.left = TreeNode(7)

a = Solution()
print(a.maxDepth3(root))


