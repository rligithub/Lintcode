class Solution1:  # bottome up dp
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        if not p:
            return False

            # dp[i][j] -- > if p[:j] can match s[:i]
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 两种case
                # CASE 1 --> NOT *
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                # CASE 2 --> *
                # 1) aaab vs a*  ==> compare * with i -1 again
                # 2) abcd vs abcd* ==> compare j-1 with i to see they all matched, * == empty
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


class Solution:  # top down dp
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
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
        if i < m and j == n:
            return False

        if i > m:
            return False

        res = False
        if i < m and j < n:
            if (s[i] == p[j] or p[j] == '?') and self.dfs(s, p, i + 1, j + 1, memo):
                res = True
                return True

        if j < n and p[j] == '*':
            if self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 1, memo):
                res = True
                return True
        memo[(i, j)] = res
        return res