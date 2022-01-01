class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        if not matrix:
            return []
        n, m = len(matrix[0]), len(matrix)
        res = None
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

                for ii in range(i):
                    for jj in range(j):
                        if dp[i][j] == dp[i][jj] + dp[ii][j] - dp[ii][jj]:
                            res = [(ii, jj), (i - 1, j - 1)]
                            return res




