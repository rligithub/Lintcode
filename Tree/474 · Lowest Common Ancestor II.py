print('474 · Lowest Common Ancestor II')

class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None



class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):

        if not root:
            return None
        PA = A
        PB = B
        while PA != PB:
            if PA.parent:
                PA = PA.parent
            else:
                PA = B
            if PB.parent:
                PB = PB.parent
            else:
                PB = A
        return PA





root = ParentTreeNode(4)
root.left = ParentTreeNode(3)
root.right = ParentTreeNode(7)
root.right.left = ParentTreeNode(5)
root.right.right = ParentTreeNode(6)
root.left.parent = root
root.right.parent = root
root.right.left.parent = root.right
root.right.right.parent = root.right
a= Solution()
A= 3
B=7
print(a.lowestCommonAncestorII(root,A,B))
