class Solution1:  # bottom up
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[0][0]
                    continue
                if (i == 0 or j == 0) and matrix[i][j] == 1:
                    dp[i][j] = 1
                if (i > 0 and j > 0) and matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j] * dp[i][j])
        return res


class Solution:  # top down (worst than bottom up dp)
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """

    def maxSquare(self, matrix):
        memo = {}
        res = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res = max(res, self.dfs(matrix, i, j, memo))
        return res * res

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        m, n = len(matrix), len(matrix[0])

        # check if 越界
        if i < 0 or i > m - 1 or j < 0 or j > n - 1:
            return 0

        res = 0
        if matrix[i][j] == 1:
            res = min(self.dfs(matrix, i + 1, j, memo), self.dfs(matrix, i, j + 1, memo),
                      self.dfs(matrix, i + 1, j + 1, memo)) + 1

        memo[(i, j)] = res
        return res
