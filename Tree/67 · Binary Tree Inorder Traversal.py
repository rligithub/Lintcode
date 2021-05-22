print('67 · Binary Tree Inorder Traversal')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    # recursion method
    def inorderTraversal(self, root):
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) +[root.val] + self.inorderTraversal(root.right)


# non-recursion method - stack
    def inorderTraversal2(self, root):
        if not root:
            return []
        stack, res =[] ,[]

        cur=root
        stack.append(cur)
        # add left node all the way down
        while cur.left:
            stack.append(cur.left)
            cur = cur.left
        # pop left node is leave, pop
        while stack:
            cur = stack.pop()
            res.append(cur.val)
        # check if there is right node, move to current node
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return res

# whileloop: go left until it's last left node
# whileloop: stack: pop() , remember current position
# If: check if there is any right node: if yes, remember current position
# Whileloop: check again: append all any child note for the current position, update current position, check left node



a =Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


print(a.inorderTraversal(root))
print(a.inorderTraversal2(root))