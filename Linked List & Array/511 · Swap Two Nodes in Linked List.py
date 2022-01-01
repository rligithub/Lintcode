
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        if not head or not head.next:
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head
        prev = dummyhead
        cur = head
        c1,c2 = None, None
        while cur:
            if cur.val == v1:
                p1 = prev
                c1 = cur
            if cur.val == v2:
                p2 = prev
                c2 = cur
            cur = cur.next
            prev = prev.next
        if c1 and c2:
            p1.next, p2.next = c2, c1
            c2.next, c1.next = c1.next, c2.next

        return dummyhead.next

'''
1->2->3->4->null
2
5
'''
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
v1 = 2
v2 = 5
a = Solution()
a.swapNodes(head, v1, v2)
cur = head
while cur:
    print (cur.val)
    cur = cur.next