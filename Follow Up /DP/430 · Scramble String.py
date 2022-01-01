class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    def isScramble(self, s1, s2):
        memo = {}
        return self.dfs(s1, s2, memo)

    def dfs(self, s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if s1 == s2:
            memo[(s1, s2)] = True
            return True
        if sorted(s1) != sorted(s2) or len(s1) != len(s2):
            memo[(s1, s2)] = False
            return False

        for i in range(1, len(s1)):
            if (self.dfs(s1[:i], s2[:i], memo) and self.dfs(s1[i:], s2[i:], memo)) or (
                    self.dfs(s1[:i], s2[-i:], memo) and self.dfs(s1[i:], s2[:-i], memo)):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False

