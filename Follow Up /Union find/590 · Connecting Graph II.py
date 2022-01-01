class ConnectingGraph2:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        self.table = {num: num for num in range(1, n + 1)}
        self.nodeNum = {num: 1 for num in range(1, n + 1)}

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota != rootb:
            self.table[roota] = rootb
            self.nodeNum[rootb] += self.nodeNum[roota]

    """
    @param: a: An integer
    @return: An integer
    """

    def query(self, a):
        return self.nodeNum[self.find(a)]

    def find(self, a):
        if self.table[a] == a:
            return a
        self.table[a] = self.find(self.table[a])
        return self.table[a]

