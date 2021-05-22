print('596 · Minimum Subtree')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        self.min_weight = float('inf')
        self.min_tree_node = None

        self.helper(root)
        return self.min_tree_node

    def helper(self,root):
        if not root:
            return 0
        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        tree_weight = left_weight + right_weight + root.val

        if tree_weight < self.min_weight:
            self.min_weight = tree_weight
            self.min_tree_node = root

        return tree_weight





root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(-5)
root.left.left= TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(-4)
root.right.right = TreeNode(-5)
a=Solution()
print(a.findSubtree(root))