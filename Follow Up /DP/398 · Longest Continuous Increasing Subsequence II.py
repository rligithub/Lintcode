class Solution: # top down DP ==> DFS + Memory
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, matrix):
        # DFS + memory ==> Top down DP
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        longest = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                longest = max(longest, self.dfs_memo(memo, matrix, i, j))
        return longest

    def dfs_memo(self, memo, matrix, x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        longest = 1
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx, yy = x + dx, y + dy

            if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[0]) and matrix[xx][yy] > matrix[x][y]:
                longest = max(longest, 1 + self.dfs_memo(memo, matrix, xx, yy))
        memo[(x, y)] = longest
        return longest


class Solution2:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 1
        memo = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs_memo(memo, matrix, i, j))
        return res

    def dfs_memo(self, memo, matrix, x, y):
        if memo[x][y] !=0:

            return memo[x][y]

        res = 1
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx, yy = x + dx, y + dy

            if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[0]) and matrix[xx][yy] > matrix[x][y]:
                res = max(res, 1 + self.dfs_memo(memo, matrix, xx, yy))
        memo[x][y] = res
        return res



matrix= [[1,3,2],[4,6,5],[7,9,8],[13,15,14],[10,12,11]]

a = Solution()
print(a.longestContinuousIncreasingSubsequence2(matrix))