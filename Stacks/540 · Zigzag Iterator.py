class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        # do intialization if necessary

        self.queue = collections.deque()
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            self.queue.append(v1[i])
            self.queue.append(v2[j])
            i += 1
            j += 1
        while i < len(v1):
            self.queue.append(v1[i])
            i += 1
        while j < len(v2):
            self.queue.append(v2[j])
            j += 1

    """
    @return: An integer
    """

    def _next(self):
        # write your code here
        return self.queue.popleft()

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        return self.queue

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result