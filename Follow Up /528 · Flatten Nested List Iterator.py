"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""
import collections


class NestedIterator(object):

    def __init__(self, nestedList):
        self.queue = collections.deque()
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.queue.append(item.getInteger())
            else:
                self.flatten(item.getList())

    # @return {int} the next element in the iteration
    def next(self):
        if self.hasNext:
            return self.queue.popleft()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        return self.queue

    # Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())