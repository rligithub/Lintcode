
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next   # please note that slow pointer should be before mid pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next # mid point 
        slow.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

head = ListNode(-1)
head.next = ListNode(1)
head.next.next = None

a = Solution()
a.sortedListToBST(head)