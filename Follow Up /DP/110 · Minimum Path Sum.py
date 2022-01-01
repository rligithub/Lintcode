class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        #dp[i] represents minimum sum of path --> depends on dp[i-1][j] and dp[i][j-1]
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for i in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
