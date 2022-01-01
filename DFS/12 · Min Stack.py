class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    # do intialization if necessary

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)
        if not self.minStack or number <= self.minStack[-1]:
            self.minStack.append(number)

    """
    @return: An integer
    """

    def pop(self):
        if self.stack:
            num = self.stack.pop()
            if num == self.minStack[-1]:
                self.minStack.pop()
            return num
        else:
            return

    """
    @return: An integer
    """

    def min(self):
        if self.minStack:
            return self.minStack[-1]



stack=[]
stack.append(3)
stack.append(1)

a = MinStack()

a.push(1)
print(a.min())
a.push(2)
print(a.min())
a.push(3)
print(a.min())