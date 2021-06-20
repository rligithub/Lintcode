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
        #step1 - check if both A and B exist in the tree
        #step2 - if yes, run classic LCA solution
        self.foundA = False
        self.foundB = False

        res = self.LCA(root,A,B)
        if not self.foundA or not self.foundB:
            return None
        else:
            return res

    def LCA(self,root,A, B):
        if not root:
            return None
        left = self.LCA(root.left,A,B)
        right = self.LCA(root.right,A,B)

        if root == A:
            self.foundA =True
            return root
        if root == B:
            self.foundB = True
            return root

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right

        return None




root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(7)
A= root.right.left = TreeNode(5)
B= root.right.right = TreeNode(6)
a= Solution()

print(a.lowestCommonAncestor3(root,A,B).val)
