print('376 · Binary Tree Path Sum')


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
    def binaryTreePathSum(self, root, target):
        if not root:
            return None
        path,res=[],[]
        self.helper(root, target, path, 0, res)
        return res

    def helper(self,root,target, path, summ, res):
        if not root:
            return
        path.append(root.val)
        summ += root.val
        if not root.left and not root.right and summ == target:
            res.append(path[:])

        self.helper(root.left, target, path, summ, res)
        self.helper(root.right, target, path, summ, res)

        path.pop()




root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right = TreeNode(3)
target = 5
a = Solution()
print(a.binaryTreePathSum(root,target))