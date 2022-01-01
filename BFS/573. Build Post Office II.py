import collections


class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # Record dist sum from houses to each empty lands, record how many houses can be reached to each empty lands
        # BFS --> 对于每个house找相邻的所有空地，保存 每块空地到这个house的距离 和 每块空地能到达的house数
        # for loop to find the where to build the post office:
        # 1. empty lands -->  grid[x][y] == 0
        # 2. can reach to each houses  --> reach[x][y] = houses_num
        # 3. with min sum distances --> res = min(distances[x][y])

        if not grid:
            return 0

        m,n = len(grid),len(grid[0])
        houses_num = 0
        distances = collections.defaultdict(int)
        reach = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    houses_num += 1
                    self.bfs(grid, i,j,distances, reach)

        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[(i,j)] == houses_num:
                    res = min(res, distances[(i,j)])

        if res < float('inf'):
            return res
        else:
            return -1

    def bfs(self,grid,i,j,distances,reach):

        m,n = len(grid),len(grid[0])
        queue = collections.deque()
        queue.append([i, j, 0])
        visited = set()
        visited.add((i, j))
        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0 and (xx, yy) not in visited:
                    reach[(xx, yy)] += 1
                    queue.append([xx, yy, dist + 1])
                    distances[(xx, yy)] += dist + 1
                    visited.add((xx,yy))





grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]

a = Solution()
print(a.shortestDistance(grid))