from lintcode import (
    ListNode,
)

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """

    def reorderList(self, head):
        # step1: find the middle node of the linked list
        # step2: reverse the 2nd half
        # merge two linked list into one long linked list

        if not head or not head.next:
            return

            # 把mid 放在前半部分
        # find the mid
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid, mid_next = slow, slow.next
        mid.next = None

        # reverse 2nd half
        cur, prev = mid_next, None
        while cur:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        # merge 1st half & second half
        while head and prev:
            head_next, prev_next = head.next, prev.next

            head.next = prev
            prev.next = head_next

            head, prev = head_next, prev_next

        return
