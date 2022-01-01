"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head node
    @return: the middle node
    """

    def middleNode(self, head):
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow