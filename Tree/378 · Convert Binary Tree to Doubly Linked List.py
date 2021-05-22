print('378 · Convert Binary Tree to Doubly Linked List')

class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = None
        self.prev = None
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):

        return self.helper(root)[0]

    def helper(self,root):
        if not root:
            return None

        left_last = self.helper(root.left)
        right_last = self.helper(root.right)

        node = DoublyListNode(root.val)

        if left_last:
            left_last.next = root.right
            root.right.prev= left_last

            root.next = root.left
            root.left.prev = root
            root.left = None
            root.right = None
        return right_last or left_last or root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

a= Solution()
print(a.bstToDoublyList(root))