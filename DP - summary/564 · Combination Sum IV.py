class Solution: #1D --> DP 无限次使用item，排列顺序重要
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        if not nums or not target:
            return 0

        m = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        # i --> number of item
        # j --> size of backpack
        # dp[j] = dp[j - nums[0]] + dp[j - nums[1]] ... + dp[j - nums[m-1]]
        # 求dp[j] --> 回头看所有可能性，以dp[j]为行数，看每行的每一个的关系
        for j in range(1, target + 1):
            for i in range(m):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        return dp[-1]


class Solution2: # top down dp
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        if not nums or not target:
            return 0

        memo = {}
        # 可以重复利用同一个item，dp[i]需要回头看1...n个items的总和 --> dfs需要一个for loop
        return self.dfs(nums, target, memo)

    def dfs(self, nums, target, memo):
        if target in memo:
            return memo[target]

        if target == 0:
            return 1
        if target < 0:
            return 0

        # res是每一层的总和，每层reset
        res = 0
        for num in nums:
            res += self.dfs(nums, target - num, memo)

        memo[target] = res
        return memo[target]