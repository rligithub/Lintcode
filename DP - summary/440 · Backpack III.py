class Solution1:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        if not A or not m:
            return 0

            # n --> number of items
        # m --> size of backpack
        n = len(A)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # i --> number of items
        # j --> size of backpack
        for i in range(m + 1):
            for j in range(n):
                if A[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])

        return max(dp[-1])


class Solution2:  # top-down dp
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        if not A or not m:
            return 0
        memo = {}
        return self.dfs(A, V, 0, m, memo)

    def dfs(self, A, V, pos, weight, memo):
        if (pos, weight) in memo:
            return memo[(pos, weight)]

        if pos > len(A) - 1:
            return 0

        pick = 0
        if weight - A[pos] >= 0:
            pick = self.dfs(A, V, pos, weight - A[pos], memo) + V[pos]
        not_pick = self.dfs(A, V, pos + 1, weight, memo)

        memo[(pos, weight)] = max(pick, not_pick)
        return memo[(pos, weight)]


class Solution: # 滚动数组
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        if not A or not m:
            return 0

            # n --> number of items
        # m --> size of backpack
        n = len(A)
        dp = [0] * (m + 1)

        # i --> number of items
        # j --> size of backpack
        for i in range(n + 1):
            for j in range(m + 1):
                if A[i - 1] <= j:
                    dp[j] = max(dp[j], dp[j - A[i - 1]] + V[i - 1])

        print(dp)
        return max(dp)
