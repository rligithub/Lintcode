"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    # math proof:
    # assume length before circle is x, circle length is y
    # assume both fast and slow pointers meet at length m point
    # meetpoint--> slow == fast;  slow = x + m, fast = (x+y)/2 + m/2
    # end point --> slow = x + m + x, fast = (x+y)/2 + m/2 + (y-m)
    # proved: formulate at meetpoint == formulate at end point

    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """

    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        if fast and slow is fast:
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None






