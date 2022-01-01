class Solution:  # 2D dp -- > MLE
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
        if not nums or not target:
            return 0

        # dp[i][j] --> number of way to fill backpack with target size

        # i --> number of items
        # j --> size of backpack
        m = len(nums)
        dp = [[0] * (target + 1) for _ in range(m + 1)]

        # initiation must be 1
        dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(0, target + 1):
                # if current item is oversized
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
        print(dp)
        return dp[-1][-1]


class Solution2: # 1D dp --> compressed dp
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
        if not nums or not target:
            return 0

        # i --> number of items
        # j --> size of backpack
        # dp[j] --> number of methods that fill out j-sized backpack
        dp = [0] * (target + 1)

        # initialization should be 1
        dp[0] = 1
        m = len(nums)
        for i in range(m):
            for j in range(target, 0, -1):
                # 如果当前item比背包j大，dp[j]还是之前的dp[j] --> 不作为
                # 如果当前item比背包j小等，dp[j] = 旧dp[j] + 旧dp[j-item]
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[-1]


class Solution3: # top down dp
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
        if not nums or not target:
            return 0
        memo = {}
        # pos --> for loop
        # ending point --> target == 0 or pos > len(nums)-1
        # return value --> see what should we return when it gets ending point
        return self.dfs(nums, 0, target, memo)

    def dfs(self, nums, pos, target, memo):
        if (pos, target) in memo:
            return memo[(pos, target)]

        # ending point --> fill out backpack, method +1
        if target == 0:
            return 1

        if pos > len(nums) - 1:
            return 0

        # two cases
        take = self.dfs(nums, pos + 1, target - nums[pos], memo)
        not_take = self.dfs(nums, pos + 1, target, memo)

        # what is the relationship between two cases --> value saved in memo
        memo[(pos, target)] = take + not_take
        return memo[(pos, target)]



