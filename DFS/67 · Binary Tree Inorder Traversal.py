

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution1: # recursion
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right

class Solution2: # use stack
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        if not root:
            return []
        stack, res = [], []
        cur = root
        stack.append(cur)
        while cur.left:
            stack.append(cur.left)
            cur = cur.left
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return res



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
a = Solution2()
print(a.inorderTraversal(root))