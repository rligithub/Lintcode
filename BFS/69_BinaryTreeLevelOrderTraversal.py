
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        if not root:
            return []
        queue=[]
        res=[]
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level.append(cur.val)

            res.append(level)
        return res

root = TreeNode(1)
root.right =TreeNode(3)
root.left = TreeNode(2)
a=Solution()

print(a.levelOrder(root))

