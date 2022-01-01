class Solution: # bottom up dp
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    def isScramble(self, s1, s2):
        # corner case
        if len(s1) != len(s2):
            return False
        n = len(s1)

        # i --> start index in s1
        # j --> start index in s2
        # w --> length of substring for s1 and s2
        # dp[i][j][w] --> 判断 s1以i为起点长度为w的子字符 是否和 s2以j为起点长度为w的子字符 相等

        # w 长度 为 0 到 n --> 所以是 n+1
        dp = [[[False] * (n + 1) for _ in range(n)] for __ in range(n)]

        # 长度 == 1
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

                    # 长度 == 2 ... n
        # 注意i 和j 的取值范围
        for k in range(2, n + 1):
            for i in range(n - (k - 1)):
                for j in range(n - (k - 1)):
                    for w in range(1, k):
                        # 两种情况
                        # CASE 1: s11 == s21 and s12 == s22
                        # CASE 2: s11 == s22 and s12 == s21
                        if dp[i][j][w] and dp[i + w][j + w][k - w] or dp[i][j + k - w][w] and dp[i + w][j][k - w]:
                            dp[i][j][k] = True
                            break
        return dp[0][0][-1]


class Solution2: # top down dp
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        memo = {}
        return self.dfs(s1, s2, memo)

    def dfs(self, s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if (self.dfs(s1[:i], s2[:i], memo) and self.dfs(s1[i:], s2[i:], memo)) or (
                    self.dfs(s1[:i], s2[-i:], memo) and self.dfs(s1[i:], s2[:-i], memo)):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False


