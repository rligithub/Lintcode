class MinStack:
    # maintain a globalmin and save it with each number in stack

    def __init__(self):
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        if self.stack:
            globalmin = min(number, self.stack[-1][1])
        else:
            globalmin = number
        self.stack.append((number, globalmin))

    """
    @return: An integer
    """

    def pop(self):
        num, globalmin = self.stack.pop()
        return num

    """
    @return: An integer
    """

    def min(self):
        return self.stack[-1][1]

