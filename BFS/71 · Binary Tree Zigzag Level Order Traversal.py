

import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res, queue = [] , collections.deque()
        level = 0

        queue.append(root)

        while queue:
            size = len(queue)
            level_res = []
            level += 1
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level_res.append(cur.val)
            if level % 2 == 0:
                level_res = level_res[::-1]
            res.append(level_res)

        return res

root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

a = Solution()

print(a.zigzagLevelOrder(root))