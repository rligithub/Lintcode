print('88 · Lowest Common Ancestor of a Binary Tree')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # use DFS
        # base case - no root or root == A or root == B
        # case1: no root.left and root.right, return none
        # case2: only have root.left or root.right, return left or right
        # case3: have both root.left and root.right, return root
        if not root or root == A or root == B:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right,A, B)
        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            return None



root = TreeNode(4)
A = root.left = TreeNode(3)
root.right = TreeNode(7)
B = root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
a = Solution()


print(a.lowestCommonAncestor(root,A,B).val)
