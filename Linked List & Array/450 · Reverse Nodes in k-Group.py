"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        return self.reverseLinkedlist(head, k, size)


    def reverseLinkedlist(self,head, k, size):
        # base case
        if not head or size < k:
            return head
        # recursion rule
        prev, cur = None, head
        for i in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head.next = self.reverseLinkedlist(cur, k, size - k)

        return prev



