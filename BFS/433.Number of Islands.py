import collections


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = collections.deque([(i, j)])
                    grid[i][j] = 0
                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xx, yy = x + dx, y + dy
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
                                q.append((xx, yy))
                                grid[xx][yy] = 0
                    count += 1
        return count



grid = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]

grid2 = [[1]]
a= Solution()
print(a.numIslands(grid2))
