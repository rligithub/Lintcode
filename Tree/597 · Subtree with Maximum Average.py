print('597 · Subtree with Maximum Average')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    # Please note that the size of each subtree is difference
    # Compare each subtree's average value to max average value (default max avg val = infinite)
    # Update max average value and max avg root after comparison
    # Need to consider two variables (sum of subtree value, size of subtree) to calculate average val
    def findSubtree2(self, root):

    # Or set the max_avg_sum and max_avg_size as None.
    # add another condition if max value is none, current value = max value

        self.max_avg_root = None
        self.max_avg_sum = float('-inf')
        self.max_avg_size = 1

        size, avg_val = self.helper(root)
        return self.max_avg_root

    def helper(self,root):
        if not root:
            return 0, 0
        left_size,left_val = self.helper(root.left)
        right_size,right_val = self.helper(root.right)
        size = 1 + left_size + right_size
        sum_val = root.val + left_val + right_val

        if sum_val * self.max_avg_size > self.max_avg_sum * size:
            self.max_avg_sum = sum_val
            self.max_avg_size =size
            self.max_avg_root = root

        return size, sum_val




root = TreeNode(1)
root.left = TreeNode(-10)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(-4)
root.right.right = TreeNode(-1)

a=Solution()
print(a.findSubtree2(root))
