print('480 · Binary Tree Paths')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths =[]
        self.helper(root, paths)
        return paths


    def helper(self,root, paths):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        left_path = self.binaryTreePaths(root.left)
        right_path = self.binaryTreePaths(root.right)
        for path in left_path:
            paths.append(str(root.val)+'->' + path)
        for path in right_path:
            paths.append(str(root.val)+'->' + path)
        return paths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)

a=Solution()
print(a.binaryTreePaths(root))