class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        if not nums:
            return 0
        nums = [1] + nums + [1]
        memo = {}
        return self.dfs(nums, 0, len(nums) -1, memo)

    def dfs(self, nums, l, r, memo):
        if (l, r) in memo:
            return memo[(l, r)]
        if l >= r:
            return 0

        res = 0
        for k in range(l+1, r):
            res = max(res, nums[l] * nums[k] * nums[r] + self.dfs(nums, l, k, memo) + self.dfs(nums, k, r, memo))
        memo[(l, r)] = res
        return memo[(l, r)]

nums = [4, 1, 5, 10]
a = Solution()
print(a.maxCoins(nums))