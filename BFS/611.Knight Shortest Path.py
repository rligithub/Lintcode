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
        while queue:
            x,y,z = queue.popleft()
            if x == a and y == b:
                return z
            for dx, dy in (1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1):
                xx = x + dx
                yy = y + dy
                if 0<= xx < m and 0<= yy < n and grid[xx][yy] ==0:
                    grid[xx][yy] =2
                    queue.append([xx,yy,z+1])
        if grid[a][b] == 2:
            return z
        else:
            return -1


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
# DIRECTIONS = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2, 1), (-2,1)]
DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
from collections import deque


class Solution2:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        days = {(source.x, source.y): 0}
        if (source.x, source.y) == (destination.x, destination.y):
            return days[(source.x, source.y)]
        queue = deque([(source.x, source.y)])

        while queue:
            # print(days)
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if self.valid(grid, next_x, next_y) and (next_x, next_y) not in days:
                    days[(next_x, next_y)] = days[(x, y)] + 1
                    if (next_x, next_y) == (destination.x, destination.y):
                        return days[(next_x, next_y)]

                    queue.append((next_x, next_y))
        return -1

    def valid(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
            return True
        return False

grid = [[0,0,0,0,1,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,1,0,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1]]
source = Point(0,0)
destination = Point(7,0)

a = Solution()
print(a.shortestPath(grid,source,destination))







