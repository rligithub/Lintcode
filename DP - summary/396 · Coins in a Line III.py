class Solution:  # bottom up dp
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        if not values:
            return True

            # dp[i][j] means how much more money that the first player took from coin i to coin j
        # dp[i][j] --> money difference between first and second players
        # dp[i][j] >= 0 ---> first player wins
        n = len(values)

        dp = [[0] * n for _ in range(n)]

        # 长度 == 1，dp[i][j]存的值是价值差 --> 就是本身价值
        for i in range(n):
            dp[i][i] = values[i]

        # 长度 == 2 到 n
        for length in range(2, n + 1):
            for i in range(n - (length - 1)):
                j = i + length - 1
                # compare results for getting left coin vs results for getting right coin
                dp[i][j] = max(values[i] - dp[i + 1][j], values[j] - dp[i][j - 1])

        return dp[0][-1] >= 0


class Solution2: # top down dp
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        memo = {}
        return self.dfs(values, 0, len(values) - 1, memo) >= 0

    def dfs(self, values, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        pick_left = values[i] - self.dfs(values, i + 1, j, memo)
        pick_right = values[j] - self.dfs(values, i, j - 1, memo)

        memo[(i, j)] = max(pick_left, pick_right)
        return memo[(i, j)]