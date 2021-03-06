print('453 · Flatten Binary Tree to Linked List')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    # Divide and Conquer: Insert root.left node to the right.

    def flatten(self, root):
        return self.helper(root)


    def helper(self,root):
        if not root:
            return None
        # 左半部分的最后一个node （linkedlist的末尾node）
        left_last = self.helper(root.left)
        # 右半部分的最后一个node （linkedlist的末尾node）
        right_last = self.helper(root.right)

        if left_last:
            # 左孩子的右边（next）指向 右孩子
            left_last.right = root.right
            # 父节点的右边（next）指向 左孩子
            root.right = root.left
            # 父节点的左边 断开
            root.left =None
m
        return right_last or left_last or root



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

a=Solution()
print(a.flatten(root))
