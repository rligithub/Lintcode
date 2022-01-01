class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def maxKilledEnemies(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        # res = max enemies killed from up, down, left, and right
        # up[i][j] -- > max enemies killed from up direction
        # down[i][j] -- > max enemies killed from down direction
        # left[i][j] -- > max enemies killed from left direction
        # right[i][j] -- > max enemies killed from right direction

        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        # CASE1 - down direction
        # base case - if empty /wall --> 0 ; if enemy --> 1
        for j in range(n):
            if grid[0][j] == 'E':
                down[0][j] = 1
            else:
                down[0][j] = 0

                # if empty --> prev ; if wall --> 0 ; if enemy --> prev + 1
        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 'E':
                    down[i][j] = down[i - 1][j] + 1
                elif grid[i][j] == 'W':
                    down[i][j] = 0
                else:
                    down[i][j] = down[i - 1][j]

                    # CASE2 - up direction
        # base case - if empty /wall --> 0 ; if enemy --> 1
        for j in range(n):
            if grid[-1][j] == 'E':
                up[-1][j] = 1
            else:
                up[-1][j] = 0

                # if empty --> prev ; if wall --> 0 ; if enemy --> prev + 1
        for i in range(m - 2, -1, -1):
            for j in range(n):
                if grid[i][j] == 'E':
                    up[i][j] = up[i + 1][j] + 1
                elif grid[i][j] == 'W':
                    up[i][j] = 0
                else:
                    up[i][j] = up[i + 1][j]

                    # CASE3 - left direction
        # base case - if empty /wall --> 0 ; if enemy --> 1
        for i in range(m):
            if grid[i][0] == 'E':
                left[i][0] = 1
            else:
                left[i][0] = 0

                # if empty --> prev ; if wall --> 0 ; if enemy --> prev + 1
        for i in range(m):
            for j in range(1, n):
                if grid[i][j] == 'E':
                    left[i][j] = left[i][j - 1] + 1
                elif grid[i][j] == 'W':
                    left[i][j] = 0
                else:
                    left[i][j] = left[i][j - 1]

                    # CASE4 - right direction
        # base case - if empty /wall --> 0 ; if enemy --> 1
        for i in range(m):
            if grid[i][-1] == 'E':
                right[i][-1] = 1
            else:
                right[i][-1] = 0

                # if empty --> prev ; if wall --> 0 ; if enemy --> prev + 1
        for i in range(m):
            for j in range(n - 2, -1, -1):
                if grid[i][j] == 'E':
                    right[i][j] = right[i][j + 1] + 1
                elif grid[i][j] == 'W':
                    right[i][j] = 0
                else:
                    right[i][j] = right[i][j + 1]

                    # RES = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        res = 0
        for i in range(m):
            for j in range(n):
                # bomb can only placed at empty cell
                if grid[i][j] == '0':
                    res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])

        return res






