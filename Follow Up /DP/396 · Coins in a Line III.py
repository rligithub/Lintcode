class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if not values:
            return False
        if len(values) <= 2:
            return True
        memo = {}
        return self.dfs(values, 0, len(values)-1, memo) > sum(values)/2

    def dfs(self, nums, l, r, memo):
        if (l, r) in memo:
            return memo[(l, r)]
        if l > r:
            return 0
        if l == r:
            return nums[l]

        left = nums[l] + min(self.dfs(nums, l+2,r, memo), self.dfs(nums, l+1, r-1, memo))
        right = nums[r] + min(self.dfs(nums, l+1, r-1,memo), self.dfs(nums, l, r-2, memo))
        memo[(l, r)] = max(left,right)
        return memo[(l, r)]

