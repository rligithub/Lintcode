class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        if n == 0:
            return 0

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


import math


class Solution2: #DFS
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1

        k = int(math.sqrt(n))
        res = float('inf')
        for i in range(k, 0, -1):
            res = min(res, self.dfs(n - i * i, memo) + 1)
        memo[n] = res
        return memo[n]


import math
print(int(math.sqrt(5)))