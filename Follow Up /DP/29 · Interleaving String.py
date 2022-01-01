class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # means that len(s3) == len(s1) + len(s2)
        # s3[i+j] == s1[i] or s3[i+j] == s2[j]; if not, dp[i][j] = False
        n, m, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False
        dp = [[True] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s2[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s1[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]) or (
                            dp[i][j - 1] and s1[j - 1] == s3[i + j - 1])
        return dp[-1][-1]

