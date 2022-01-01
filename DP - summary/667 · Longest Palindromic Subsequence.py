class Solution: # bottom up dp
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        n = len(s)
        if n == 0 or n == 1:
            return n

        # dp[i][j] --> means from index i to j, the longest palindromic subsequence

        dp = [[0] * (n) for _ in range(n)]

        # 长度 == 1
        for i in range(n):
            dp[i][i] = 1

        # 长度 == 2
        for length in range(2, n + 1):
            # i 的取值范围像 气球挤压 所剩下的空间
            for i in range(n - (length - 1)):
                # i 是初始index， j是结束index
                j = i + length - 1
                # 如果 aba中的 s[0]==s[2]，只要看dp[1][1]的位置b是不是符合
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][-1]


class Solution2: # top down dp
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        # base case
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo) + 2
        else:
            res = max(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]
