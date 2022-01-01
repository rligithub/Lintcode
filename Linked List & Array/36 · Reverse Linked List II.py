
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        dummyhead = ListNode(0)
        dummyhead.next = head
        prev, cur = dummyhead, head

        for i in range(m):
            prev = prev.next
            cur = cur.next
        prevFrozen = prev
        curFrozen = cur
        # prevFrozen ==> listnode before m-th listnode
        # curFrozen ==> m-th listnodes (lastnode of reversing linkedlist)
        prev = prev.next
        cur = cur.next
        # start from last second nodes (m+1)th ==> cur.next = prev
        for i in range(n - m):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        prevFrozen.next = prev
        curFrozen.next = cur

        return dummyhead.next



