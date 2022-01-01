class Solution1:  # bottom up
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution:  # top down
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        memo = {}

        res = 0
        for i in range(len(nums)):
            res = max(res, self.dfs(nums, i, memo) + 1)
        return res

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos > len(nums) - 1:
            return 0

        res = 0
        for i in range(pos, len(nums)):
            if nums[i] > nums[pos]:
                res = max(res, self.dfs(nums, i, memo) + 1)
        memo[pos] = res
        return res