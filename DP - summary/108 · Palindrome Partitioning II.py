class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        n = len(s)
        if n == 0 or n == 1:
            return 0

        # dp[l][r] means from if isPalindrome from index l to index r
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        for r in range(n):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l < 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
        memo = {}
        return self.dfs(s, 0, dp, memo) - 1

    def dfs(self, s, i, dp, memo):
        if i in memo:
            return memo[i]
        if i > len(s) - 1:
            return 0
        res = float('inf')
        for j in range(i, len(s)):
            if dp[i][j]: # s[i:j] == s[i:j][::-1]
                res = min(res, self.dfs(s, j + 1, dp, memo) + 1)
        memo[i] = res
        return res