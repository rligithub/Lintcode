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
        head, tail = self.helper(root)
        return head

    def helper(self, root):
        if not root:
            return None, None

        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)

        curr_node = DoublyListNode(root.val)
        curr_head = curr_node
        curr_tail = curr_node
        if left_head and left_tail:
            curr_first = left_head
            left_tail.next = curr_node
            curr_node.prev = left_tail
        if right_head and right_tail:
            curr_last = right_tail
            curr_node.next = right_head
            right_head.prev = curr_node

        return curr_head, curr_tail





root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(1)

a= Solution()
print(a.bstToDoublyList(root))