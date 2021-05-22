print('614 · Binary Tree Longest Consecutive Sequence II')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        max_len, _, _, = self.helper(root)
        return max_len

    def helper(self, root):
        if root is None:
            return 0, 0, 0

        left_len, left_down, left_up = self.helper(root.left)
        right_len, right_down, right_up = self.helper(root.right)

        down, up = 0, 0
        if root.left and root.left.val + 1 == root.val:
            down = max(down, left_down + 1)

        if root.left and root.left.val - 1 == root.val:
            up = max(up, left_up + 1)

        if root.right and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)

        if root.right and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)

        len = down + 1 + up
        len = max(len, left_len, right_len)

        return len, down, up





root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right = TreeNode(5)
a = Solution()
print(a.longestConsecutive2(root))