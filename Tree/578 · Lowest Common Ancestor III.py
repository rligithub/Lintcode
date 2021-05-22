print('578 · Lowest Common Ancestor III')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
# method 1
    def lowestCommonAncestor3(self, root, A, B):
        foundA, foundB = False, False

        res = self.helper(root,A,B)
        if foundA and foundB:
            return res
        else:
            return None

    def helper(self,root,A, B):
        if not root:
            return None
        left = self.helper(root.left,A,B)
        right = self.helper(root.right,A,B)

        if root == A or B:
            foundA = True
            foundB = True
            return root

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right

        return None

#method 2:
    def lowestCommonAncestor33(self, root, A, B):
        if not root or root == A or root ==B:
            return root
        left = self.lowestCommonAncestor33(root.left,A,B)
        right = self.lowestCommonAncestor33(root.right,A,B)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None




root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
a= Solution()
A=5
B=6
print(a.lowestCommonAncestor3(root,A,B))
