import collections

class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """

    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = collections.deque([])
        self.vecs = vecs
        # 把每行当前的坐标存入queue
        for row, vec in enumerate(vecs):
            if vec:
                self.queue.append((row, 0))
        print(self.queue)


    """
    @return: An integer
    """

    def next(self):
        # write your code here
        if not self.hasNext():
            return float('-inf')

        row, col = self.queue.popleft()
        result = self.vecs[row][col]

        # 每次pop一个值以后，查看当前行中是否还有后续值
        if col + 1 < len(self.vecs[row]):
            self.queue.append((row, col + 1))

        return result

    """
    @return: True if has next
    """

    def hasNext(self):

        return len(self.queue) > 0

vecs = [[1,2,3],[4,5,6,7],[8,9]]
a = ZigzagIterator2(vecs)
while a.hasNext():
    print(a.next())
