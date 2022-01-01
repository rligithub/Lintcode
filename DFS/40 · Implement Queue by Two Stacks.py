import collections


class MyQueue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        self.stack1.append(element)


    """
    @return: An integer
    """

    def pop(self):
        while self.stack1:
            num = self.stack1.pop()
            self.stack2.append(num)
        newNum = self.stack2.pop()
        while self.stack2:
            num = self.stack2.pop()
            self.stack1.append(num)
        return newNum


    """
    @return: An integer
    """

    def top(self):
        while self.stack1:
            num = self.stack1.pop()
            self.stack2.append(num)
        newNum = self.stack2[-1]
        while self.stack2:
            num = self.stack2.pop()
            self.stack1.append(num)
        return newNum

a = MyQueue()
a.push(1)
print(a.pop())
a.push(2)
a.push(3)
print(a.top())
print(a.pop())