class Solution1:  # bottom up dp
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        m, n = len(s), len(p)

        # dp[i][j] --> if p[:j] is matched to s[:i]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 如果当前为*，dp[i][j]满足一个条件即可
                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        dp[i][j] |= dp[i - 1][j]  # 继续跟*比较，*可以代表有很多个
                    dp[i][j] |= dp[i][j - 2]

        return dp[-1][-1]


class Solution:  # top down dp
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s), len(p)
        if i == m and j == n:
            return True

        if j < n - 1 and p[j + 1] == '*':
            if self.matched(s, p, i, j) and self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 2, memo):
                memo[(i, j)] = True
                return True
        if self.matched(s, p, i, j) and self.dfs(s, p, i + 1, j + 1, memo):
            memo[(i, j)] = True
            return True
        memo[(i, j)] = False
        return False

    def matched(self, s, p, i, j):
        if i == len(s) or j == len(p):
            return False
        return s[i] == p[j] or p[j] == '.'
