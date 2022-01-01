
#This is the interface that allows for creating nested lists.
#You should not implement it, or speculate about its implementation

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



class NestedIterator(object):

    def __init__(self, nestedList):

    # Initialize your data structure here.
        self.stack = nestedList[::-1]
    # @return {int} the next element in the iteration
    def next(self):
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:len(self.stack)-1]+top.getList()[::-1]
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

"""
1212[12[12]12]12[12]12

"""


list = [[1, 1], 2, [1, 1]]
a = NestedIterator()
print(a.next())