
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        # let fast pointer run k times quicker than slow pointer
        # be aware of corner case
        # add another corner case for k >> size, k = k % size
        if not head or not head.next:
            return head
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        k = k % size

        if k == 0:
            return head

        fast = head
        for i in range(k - 1):
            fast = fast.next
        prev = ListNode(0)
        slow = head
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = None
        fast.next = head

        return slow





