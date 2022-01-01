class Solution:
    # 把所有被“X”包围的”O“ 变成”X“
    # 两周可能性， 所有靠边的“O”为一个大集合 --> 变不了； 不靠边的所有“0”且没有大集合里 ->变成"X“
    # for loop -->  union all "O" in i == 0, i = m -1, j = 0, j = n - 1 to XYZ
    #           --> union all middle "O" with surrounded "O", four directions
    # for loop -> find the i == "O" and parent[i] != XYZ, change it it to "X"
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        if len(board) <= 2 or len(board[0]) <= 2:
            return
            # m == row, n == column
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n + 1)
        # i == row, j == column
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    uf.union(i * n + j, m * n)
                else:
                    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        x = i + dx
                        y = j + dy
                        if board[x][y] == "O":
                            uf.union(i * n + j, x * n + y)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and uf.find(i * n + j) != m * n:
                    board[i][j] = "X"


class UnionFind:
    def __init__(self, n):
        self.parent = [num for num in range(n)]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            self.parent[min(rootx, rooty)] = max(rootx, rooty)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
