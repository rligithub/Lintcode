print('66 · Binary Tree Preorder Traversal')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    # Recursion
    def preorderTraversal(self, root):

        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)



    # non-recursion (stack)
    def preorderTraversal2(self,root):
        if root is None:
            return []
        stack =[]
        output =[]
        stack.append(root)

        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

a = Solution()
print(a.preorderTraversal(root))
print(a.preorderTraversal2(root))


