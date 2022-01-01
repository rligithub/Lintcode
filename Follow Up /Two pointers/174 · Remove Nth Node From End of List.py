"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution: # delete nth nodes from the end
    # use two pointers (don't need to get the length of linkedlist)
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if n == 0 or not head:
            return head
        dummyhead = ListNode(None)
        dummyhead.next = head
        slow, fast = dummyhead, dummyhead
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # only delete one node
        return dummyhead.next
