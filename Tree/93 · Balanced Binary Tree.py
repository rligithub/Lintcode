print('93 · Balanced Binary Tree')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
# method 1: two recursions
    # get height of left node and right node
    # compare of height of each left node and right node (return boolean)
    def isBalanced(self, root):
        if not root:
            return True

        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        return abs(self.helper(root.left) -self.helper(root.right)) <= 1


    def helper(self,root):
        if not root:
            return 0

        left_height = self.helper(root.left)
        right_height = self.helper(root.right)

        return 1 + max(left_height, right_height)

# method 2: one recursion
    # check if each subtree is a balanced tree by setting two variables (height,boolean),  return boolean only
    def isBalanced2(self, root):
        is_balanced, height = self.helper2(root)

        return is_balanced

    def helper2(self, root):
        if not root:
            return True, 0

        is_left_balanced,left_height = self.helper2(root.left)
        is_right_balanced,right_height = self.helper2(root.right)
        height = 1+ max(left_height,right_height)

        if not is_left_balanced or not is_right_balanced:
            return False, height

        if abs(left_height - right_height) >1:
            return False, height

        return True, height


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

a= Solution()
print(a.isBalanced2(root))
