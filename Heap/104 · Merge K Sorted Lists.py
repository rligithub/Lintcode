"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None 
        if len(lists) == 1:
            return lists[0]
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        head = dummyhead = ListNode(None)
        while heap:
            head.next= ListNode(heapq.heappop(heap))
            head = head.next

        return dummyhead.next
