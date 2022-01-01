class Solution1: # TLE
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):

        res = []
        for word in words:
            if self.editdistance(word, target) <= k:
                res.append(word)
        return res

    def editdistance(self, word, target):
        n, m = len(target), len(word)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):

        res = []
        for word in words:
            if self.dfs(word, target, dict()) <= k:
                res.append(word)
        return res

    def dfs(self, word, target, memo):
        if (word, target) in memo:
            return memo[(word, target)]
        if word == target:
            return 0
        if not word:
            return len(target)
        if not target:
            return len(word)

        if word[0] == target[0]:
            memo[(word, target)] = self.dfs(word[1:], target[1:], memo)
            return memo[(word, target)]
        memo[(word, target)] = min(
            self.dfs(word[1:], target[1:], memo) + 1,
            self.dfs(word[1:], target, memo) + 1,
            self.dfs(word, target[1:], memo) + 1,
        )
        return memo[(word, target)]



