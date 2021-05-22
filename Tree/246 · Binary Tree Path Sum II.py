print('246 · Binary Tree Path Sum II')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        res,path = [],[]
        if not root:
            return res
        self.helper(root, path, res, 0, target)
        return res

    def helper(self, root, path, res, l, target):
        if not root:
            return
        path.append(root.val)
        tmp = target
        for i in range(l, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                res.append(path[i:])

        self.helper(root.left, path, res, l + 1, target)
        self.helper(root.right, path, res, l + 1, target)

        path.pop()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.left.left = TreeNode(4)
target = 6

a = Solution()
print(a.binaryTreePathSum2(root, target))