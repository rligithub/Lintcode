class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        if not A or not m:
            return 0
        if sum(A) <= m:
            return sum(A)
        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 如果当前数字 大于 target；不取当前数，直接看上一个数字
                if A[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # get max of {previous dp which not include current value, or previous dp (target-current value) + current value}
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])

        return dp[-1][-1]

