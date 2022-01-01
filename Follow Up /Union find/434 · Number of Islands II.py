"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution1:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        # write your code here
        if not n or not m:
            return []

        res = []
        count = 0
        visited = set()
        self.father = {}
        operators = [(operator.x, operator.y) for operator in operators]

        for (x, y) in operators:
            if (x, y) in self.father:
                res.append(res[-1])
                continue

            self.father[(x, y)] = (x, y)
            count += 1

            for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x_, y_ = x + dx, y + dy

                if (x_, y_) in visited:
                    root, root_ = self.find((x, y)), self.find((x_, y_))
                    if root != root_:
                        self.father[root] = root_
                        count -= 1

            visited.add((x, y))
            res.append(count)

        return res

    def find(self, n):
        path = []

        while self.father[n] != n:
            path.append(n)
            n = self.father[n]

        for i in path:
            self.father[i] = n

        return n


class UnionFind:  # union-find
    def __init__(self, n):
        self.parent = [num for num in range(1, n + 1)]
        self.count = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return
        self.parent[x] = y
        self.count -= 1

    def set_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = x
            self.count += 1


class Solution:
    def numIslands2(self, m: int, n: int, positions):

        uf = UnionFind(n * m)
        res = []
        board = [[0] * n for _ in range(m)]
        for point in positions:
            i, j = point.x, point.y
            board[i][j] = 1
            pos = i * n + j
            uf.set_parent(pos)
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                    uf.union(pos, x * n + y)
            res += [uf.count]
        return res
