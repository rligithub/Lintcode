class Solution1: # bottom up
    # 比backpack1多了个value，求value最大解
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        if not m or not A:
            return 0

        # dp[i][w] --> the max value that sized-i backpack can load
        # n --> number of items
        # m --> size of backpack
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # initialization for 0-sized backpack is -1
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for w in range(1, m + 1):
                # if item is oversized
                if A[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - A[i - 1]] + V[i - 1])
        return dp[-1][-1]


class Solution: # top down dp
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        if not m or not A:
            return 0
        memo = {}
        return self.dfs(m, 0, A, V, memo)

    def dfs(self, m, pos, A, V, memo):
        if (m, pos) in memo:
            return memo[(m, pos)]

        if m == 0:
            return 0

        if pos > len(A) - 1:
            return 0

        # ending point --> when m-sized backpack can't load more items
        # 和backpack v的题目不一样，backpack V的ending point是刚好装满的解，这个没有要求装满，而是求装不下为止的最大value解
        pick = 0
        if m - A[pos] >= 0:
            pick = self.dfs(m - A[pos], pos + 1, A, V, memo) + V[pos]
        not_pick = self.dfs(m, pos + 1, A, V, memo)

        memo[(m, pos)] = max(pick, not_pick)
        return memo[(m, pos)]


m = 1000
A = [88,85,59,100,94,64,79,75,18,38,47,11,56,12,96,54,23,6,19,31,30,32,21,31,4,30,3,12,21,60,42,42,78,6,72,25,96,21,77,36,42,20,7,46,19,24,95,3,93,73,62,91,100,58,57,3,32,5,57,50,3,88,67,97,24,37,41,36,98,52,75,7,57,23,55,93,4,17,5,13,46,48,28,24,70,85,48,48,55,93,6,8,12,50,95,66,92,25,80,16]
V = [53,70,20,41,12,71,37,87,51,64,63,50,73,83,75,60,96,70,76,25,27,89,93,40,41,89,93,46,16,4,41,29,99,82,42,14,69,75,20,20,56,23,92,71,70,1,63,18,11,68,33,6,82,69,78,48,95,42,53,99,15,76,64,39,48,83,21,75,49,73,85,28,31,86,63,12,71,35,21,17,73,18,7,51,94,88,46,77,80,95,31,80,32,45,5,30,51,63,43,9]

a = Solution()
print(a.backPackII(m, A, V))