class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # corner case
        if not A or not B:
            return 0

            # dp[i][j] --> the longest common subsequence for A[:i] and B[:j]
        n, m = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[j - 1] == B[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


class Solution2:  # top down
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        memo = {}
        return self.dfs(A, B, 0, 0, memo)

    def dfs(self, A, B, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # stop point
        if i > len(B) - 1 or j > len(A) - 1:
            return 0

            # base case
        if A[i] == B[j]:
            res = self.dfs(A, B, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(A, B, i + 1, j, memo), self.dfs(A, B, i, j + 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]