class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        if not S:
            return 0
        if not T:
            return 1
        n, m = len(T), len(S)

        dp = [[0] * (1 + n) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if T[j - 1] == S[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # no increase functions
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


