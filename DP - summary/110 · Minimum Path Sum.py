class Solution1:  # 2D dp
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # corner case
        if not grid:
            return 0

            # dp[i][j] --> min path sum from point[0][0] to point[i][j]
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # base case
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            for j in range(1, n):
                dp[0][j] = dp[0][j - 1] + grid[0][j]
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


class Solution:  # rolling 1D dp
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        if not grid:
            return 0
            # dp[i][j] --> min path sum from point[0][0] to point[i][j]
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            dp[0] += grid[i][0]

            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]

