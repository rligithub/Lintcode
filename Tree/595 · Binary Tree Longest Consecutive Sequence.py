print('595 · Binary Tree Longest Consecutive Sequence')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        self.longestpath = 0
        self.helper(root)
        return self.longestpath

    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        subtreelongest = 1
        if root.left and root.val +1 == root.left.val:
            subtreelongest = max(subtreelongest,left +1)
        if root.right and root.val +1 == root.right.val:
            subtreelongest =max(subtreelongest,right +1)
        if subtreelongest > self.longestpath:
            self.longestpath = subtreelongest
        return subtreelongest




root= TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right = TreeNode(5)
a= Solution()
print(a.longestConsecutive(root))

