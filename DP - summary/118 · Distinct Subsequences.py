class Solution1:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # corner case
        if not S:
            return 0
        if not T:
            return 1

            # dp[i][j] --> the num of disctinct subsequences in S[:i] and T[:j]
        m, n = len(T), len(S)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case
        dp[0][0] = 1
        for i in range(1, m + 1):
            dp[i][0] = 0
        for j in range(1, n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # CASE1 --> 找到相同字符 --> compare current i to prev index of longer str, compare prev i to prev index of longer str
                # dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                if S[j - 1] == T[i - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    # CASE 2 -> 不同字符 --> compare current i to prev index of longer str
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # corner case
        if not S:
            return 0
        if not T:
            return 1
        memo = {}
        return self.dfs(S, T, 0, 0, memo)

    def dfs(self, L, S, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # stop point
        # 短短走到头，结束一个solution， +1
        if i > len(S) - 1:
            return 1
        # 长长走到头，没有solution
        if j > len(L) - 1:
            return 0

        if S[i] == L[j]:
            res = self.dfs(L, S, i, j + 1, memo) + self.dfs(L, S, i + 1, j + 1, memo)
        else:
            res = self.dfs(L, S, i, j + 1, memo)
        memo[(i, j)] = res
        return memo[(i, j)]





