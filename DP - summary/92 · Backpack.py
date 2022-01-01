class Solution: # bottom up
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        if not m or not A:
            return 0

        if sum(A) <= m:
            return sum(A)

        # dp[i][j] --> max size of items that we can pack for backpack size i

        n = len(A)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # dp[i][j] --> max size of {includes current item} and {not includes current item}
        # i --> num of items
        # j --> size of backpack
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # current item size > current bag; can't fill
                if A[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:  # 上一层的数（背包size i） vs （上一层的数（背包size i-当前大小） + 当前大小）
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])

        return dp[-1][-1]


class Solution2: # topdown dp
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        if not m or not A:
            return 0
        memo = {}
        return self.dfs(A, m, 0, memo)

    def dfs(self, A, target, pos, memo):
        if (target, pos) in memo:
            return memo[(target, pos)]

        if pos > len(A) - 1:
            return 0

        pick = 0
        if target - A[pos] >= 0:
            pick = self.dfs(A, target - A[pos], pos + 1, memo) + A[pos]
        not_pick = self.dfs(A, target, pos + 1, memo)

        memo[(target, pos)] = max(pick, not_pick)
        return memo[(target, pos)]
