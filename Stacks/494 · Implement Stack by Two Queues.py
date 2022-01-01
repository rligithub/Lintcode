import collections


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = collections.deque()

    def push(self, x):
        return self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        if self.queue1:
            return self.queue1.pop()


    """
    @return: An integer
    """
    def top(self):
        if self.queue1:
            value = self.queue1.pop()
            self.queue1.append(value)
            return value


    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        if self.queue1:
            return False
        return True

a = Stack()
a.push(1)
a.pop()
a.push(2)
print(a.isEmpty()) # return false
print(a.top()) # return 2
a.pop()
print(a.isEmpty()) # return true