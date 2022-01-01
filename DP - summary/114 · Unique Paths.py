class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # move either down or right --> dp[i][j] depends on dp[i-1][j] and dp[i][j-1]

        dp = [[0] * n for i in range(m)]

        for i in range (m):
            for j in range(n):
                if i == 0 or j == 0 :
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]




