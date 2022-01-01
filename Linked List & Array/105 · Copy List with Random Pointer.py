
#Definition for singly-linked list with a random pointer.
import collections


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None



class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # setup a hashmap to save the Node to NodeCopy
        # for loop to copy Node.next
        # for loop to copy Node.random
        hashmap = collections.defaultdict()
        cur = head
        while cur:
            hashmap[cur] = RandomListNode(cur.label)
            cur = cur.next

        for node in hashmap:
            if node.next:
                hashmap[node].next = hashmap[node.next]
            if node.random:
                hashmap[node].random = hashmap[node.random]

        return hashmap[head]
