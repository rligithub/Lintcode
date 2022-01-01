class Solution: # TLE  - DFS w/o memo
    def firstWillWin(self, nums):

        if len(nums) <= 2:
            return True
        memo = {}
        return self.dfs(0, nums, memo) > 0

    def dfs(self, pos, nums, memo):
        if pos >= len(nums)-1:
            return nums[-1]

        one = nums[pos] - self.dfs(pos + 1, nums, memo)
        two = nums[pos] + nums[pos + 1] - self.dfs(pos + 2, nums, memo)
        return max(one, two)

class Solution1: #DP top down --> DFS with memo --> computer difference between first player and second player
    def firstWillWin(self, nums):
        # write your code here
        if len(nums) <= 2:
            return True
        memo = {}
        return self.dfs(0, nums, memo) > 0

    def dfs(self, pos, nums, memo):
        if pos in memo:
            return memo[pos]
        if pos >= len(nums) - 1:
            return nums[-1]

        one = nums[pos] - self.dfs(pos + 1, nums, memo)
        two = nums[pos] + nums[pos + 1] - self.dfs(pos + 2, nums, memo)
        memo[pos] = max(one, two)
        return memo[pos]



class Solution2: # DP Top down --> compute first player's max value only
    def firstWillWin(self, nums):
        # write your code here
        if len(nums) <= 2:
            return True
        memo = {}
        return self.dfs(0, nums, memo) > sum(nums) / 2

    def dfs(self, pos, nums, memo):
        if pos in memo:
            return memo[pos]
        if pos == len(nums) - 1:
            return nums[pos]
        if pos > len(nums) - 2:
            return 0

        one = nums[pos] + min(self.dfs(pos + 2, nums, memo), self.dfs(pos + 3, nums, memo))
        two = nums[pos] + nums[pos + 1] + min(self.dfs(pos + 3, nums, memo), + self.dfs(pos + 4, nums, memo))
        memo[pos] = max(one, two)
        return memo[pos]




nums = [100,200,400,300,400,800,500,600,1200]
a = Solution()
print(a.firstWillWin(nums))

