class Solution1:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        # corner cases
        if n == 0:
            return m
        if m == 0:
            return n

            # dp[i][j] --> the min steps to convert word2[:i] to word1[:j]

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # CASE 1 - 不操作  -> 如果最后一位字符相同，比较前面一位
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # CASE 2 - 操作
                    # 1） 增加/删掉word1的字符，word1和Word2的最后一位相同，比较前面
                    # 2） 改变word2的字符，word1和Word2的最后一位相同，比较前面
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]


class Solution2:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        memo = {}
        return self.dfs(word1, word2, len(word1) - 1, len(word2) - 1, memo)

    def dfs(self, A, B, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # base case (i, j are index, length should be +1)
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        no_action = float('inf')
        if A[i] == B[j]:
            no_action = self.dfs(A, B, i - 1, j - 1, memo)
        action = min(self.dfs(A, B, i - 1, j, memo), self.dfs(A, B, i, j - 1, memo),
                     self.dfs(A, B, i - 1, j - 1, memo)) + 1

        memo[(i, j)] = min(no_action, action)
        return memo[(i, j)]


class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, A, B, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # base case (i, j are index, length should be +1)
        if i >= len(A):
            return len(B) - j
        if j >= len(B):
            return len(A) - i

        no_action = float('inf')
        if A[i] == B[j]:
            no_action = self.dfs(A, B, i + 1, j + 1, memo)
        action = min(self.dfs(A, B, i + 1, j, memo), self.dfs(A, B, i, j + 1, memo),
                     self.dfs(A, B, i + 1, j + 1, memo)) + 1

        memo[(i, j)] = min(no_action, action)
        return memo[(i, j)]

