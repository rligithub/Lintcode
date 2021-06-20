print('1311.Lowest Common Ancestor of a Binary Search Tree')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # if p and q are less than root.val, search in root.left
        # if p and q are greater than root.val, search in root.right
        # if p < root.val < q, return root

        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

root = TreeNode(6)
p = root.left = TreeNode(2)
q = root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right =TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

a=Solution()

print(a.lowestCommonAncestor(root,p,q).val)