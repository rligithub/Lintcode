class Solution1:  # top- down dp # TLE
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        if len(nums) == 0:
            return 0
        # add two unbroken balloons in left and right
        nums = [1] + nums + [1]
        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, memo)

    def dfs(self, nums, l, r, memo):
        if (l, r) in memo:
            return memo[(l, r)]

        if l + 1 == r:
            return 0

        res = 0
        # l + 1 <= k <= r-1
        for k in range(l + 1, r):
            res = max(res, self.dfs(nums, l, k, memo) + self.dfs(nums, k, r, memo) + nums[l] * nums[k] * nums[r])

        memo[(l, r)] = res
        return memo[(l, r)]


class Solution:  # bottom up dp
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        if len(nums) == 0:
            return 0
        nums = [1] + nums + [1]

        n = len(nums)

        # dp[i][j] --> max coins we can collect from bursting buallons i to j
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(0, n - (length - 1)):
                j = i + length - 1
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])

        return dp[0][n - 1]
