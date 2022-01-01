class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        self.table = {num: num for num in range(1, n + 1)}
        self.graphNum = n

    def connect(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota != rootb:
            self.table[roota] = rootb
            self.graphNum -= 1

    """
    @return: An integer
    """

    def query(self):
        return self.graphNum

    def find(self, a):
        if self.table[a] == a:
            return a
        self.table[a] = self.find(self.table[a])
        return self.table[a]