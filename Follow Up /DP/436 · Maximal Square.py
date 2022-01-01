class Solution:
    # dp[i][j] --> represents the max size of square with the cordinate [i][j] as its bottom right corner
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]* n for i in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j]
                if i and j and dp[i][j]:
                    dp[i][j] = 1+ min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                res = max(res, dp[i][j])
        return res * res