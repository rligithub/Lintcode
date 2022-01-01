class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if not grid or not grid[0]:
            return -1

        n, m = len(grid[0]), len(grid)
        queue = collections.deque()

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    queue.append([i,j])
        day = 0

        while queue:
            size = len(queue)
            day += 1
            for k in range(size):
                x,y = queue.popleft()
                for dx,dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    xx = x + dx
                    yy = y + dy
                    if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == 0:
                        grid[xx][yy] = 1
                        queue.append([xx, yy])


        for j in range(n):
            for i in range(m):
                if grid[i][j] == 0:
                    return -1
        return day - 1



class Solution2:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # base case
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        walls = 0
        que =collections.deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    que.append([i,j,0])
                if grid[i][j] == 2:
                    walls +=1

        days = 0
        count = 0
        while que:
            x,y,z =que.popleft()
            days = max(days,z)
            count +=1
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                xx, yy = x + dx, y + dy
                if xx >= 0 and xx < n and yy >= 0 and yy < m and grid[xx][yy] == 0:
                    grid[xx][yy] = 1
                    que.append([xx,yy,z+1])  # at each point[xx,yy], update the days "z" for turning 0s to 1s

        # count == how many 1s (or 0s became 1s) popped out from queue == people + zombie
        # check if people + zombie + walls == total size of 2D matrix, if not, there must be 0s in matrix
        if count + walls == m * n:
            return days
        else:
            return -1


grid  =[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]

a= Solution2()
print(a.zombie(grid))



