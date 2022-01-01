class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        if not m or not A:
            return 0
        if sum(A) <= m:
            return sum(V)

        dp = [[0] * (m + 1) for _ in range(len(A)+1)]

        for i in range(1, len(A)+1):
            for j in range(1, m + 1):
                if A[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])

        return dp[-1][-1]

m = 10
A = [2, 3, 8]
V = [2, 5, 8]
a = Solution()
print(a.backPackII(m,A, V))