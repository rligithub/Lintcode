class Solution1:  # bottom up dp
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # compare if len(s3) == len(s1) + len(s2)
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

            # dp[i][j] --> if s3[:i+j] are consist of s1[:i] and s2[:j]
        dp = [[True] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

                # TWO CASES
                # case 1: compare s3 to s1
                # case 2: compare s3 to s2
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                            dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]


class Solution:  # top down dp
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        return self.dfs(s1, s2, s3, 0, 0, 0, memo)

    def dfs(self, s1, s2, s3, i, j, k, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # 三个走到头了 -- 结束
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
            # 如果其中两个提前走到头了 --> False
        if (i == len(s1) or j == len(s2)) and k == len(s3):
            return False
            # CASE 1:
        if i < len(s1) and s1[i] == s3[k]:
            if self.dfs(s1, s2, s3, i + 1, j, k + 1, memo):
                memo[(i, j)] = True
                return True
                # CASE 2:
        if j < len(s2) and s2[j] == s3[k]:
            if self.dfs(s1, s2, s3, i, j + 1, k + 1, memo):
                memo[(i, j)] = True
                return True
        memo[(i, j)] = False
        return False





