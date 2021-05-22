print('68 · Binary Tree Postorder Traversal')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if not root:
            return []
        stack, res = [], []
        cur = root

        while cur:
            stack.append(cur)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if stack and stack[-1].left == cur:
                cur = stack[-1].right
                while cur:
                    stack.append(cur)
                    if cur.left:
                        cur = cur.left
                    else:
                        cur = cur.right

        return res



a = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(a.postorderTraversal(root))
