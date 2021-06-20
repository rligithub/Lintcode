import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []
        queue = collections.deque()
        res = []
        dummy = ListNode(0)

        queue.append(root)

        while queue:
            curNode = dummy
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                curNode.next = ListNode(cur.val)
                curNode = curNode.next
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(dummy.next)

        return res


root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

a = Solution()
print(a.binaryTreeToLists(root))