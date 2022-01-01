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
            memo = {}
            if self.dfs(word, target, 0, 0, memo) <= k:
                res.append(word)
        return res

    def dfs(self, A, B, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        m, n = len(A), len(B)

        if i > m - 1:
            return n - j
        if j > n - 1:
            return m - i

        if A[i] == B[j]:
            res = self.dfs(A, B, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(A, B, i + 1, j + 1, memo), self.dfs(A, B, i + 1, j, memo),
                      self.dfs(A, B, i, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]

