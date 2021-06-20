import collections


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        #base case
        if not grid or source == destination:
            return 0

        m, n = len(grid), len(grid[0])
        queue = collections.deque()

        i,j = source.x, source.y
        a,b = destination.x, destination.y
        queue.append([i,j,0])
        grid[i][j] = 2
        steps = 0
        while queue:
            x,y,z = queue.popleft()
            if x == destination.x and y == destination.y:
                steps = max(steps, z)
                return steps
            for dx, dy in (1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1):
                xx = x + dx
                yy = y + dy
                if 0<= xx < m and 0<= yy < n and grid[xx][yy] == 0:
                    grid[xx][yy] =2
                    queue.append([xx,yy,z+1])
        if grid[a][b] == 2:
            return steps
        else:
            return -1




grid = [[0,0,0,0,1,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,1,0,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1]]
source = Point(0,0)
destination = Point(7,0)

a = Solution()
print(a.shortestPath(grid,source,destination))







