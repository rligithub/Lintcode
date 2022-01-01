
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
    #   quick sort:
    # step1: set two dummy head "Small" and "Large" and two moving pointer
    # step2: put all smaller nodes in small linkedlist + all larger nodes in large linkedlist
    # step3: merge two linkedlists

        dummyHeadS, dummyHeadL = ListNode(0), ListNode(0)
        small= dummyHeadS
        large = dummyHeadL
        cur = head

        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next

            else:
                large.next = cur
                large = large.next
            cur = cur.next
        small.next = dummyHeadL.next
        large.next = None

        return dummyHeadS.next

