class ConnectingGraph:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        self.table = {num: num for num in range(1, n + 1)}

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        roota, rootb = self.find(a), self.find(b)
        if roota != rootb:
            self.table[roota] = rootb

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """

    def query(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, x):

        if self.table[x] == x:
            return x
        self.table[x] = self.find(self.table[x])
        return self.table[x]
