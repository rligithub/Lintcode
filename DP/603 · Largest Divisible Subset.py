class Solution: # Time complexity = O(n^2)
    # use dp[i] represents the max length of divisible subset at index i
    # use prev[i] represents the previous position of index i
    #
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset
    """

    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)

        prev = [-1] * len(nums)  # save prev index position for current position
        maxcount, index = 0, 0
        res = []

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] >= maxcount:
                        maxcount = dp[i]  # record maxcount and its position
                        index = i

        while index != -1:
            res.append(nums[index])
            index = prev[index]  # to get the prev position in prev[]
        return res[::-1]

class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()
        res = [[num] for num in nums]  # contains sets starting with that number

        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(res[i]) < len(
                        res[j]) + 1:  # to ensure the length of the set is maximal
                    res[i] = res[j] + [nums[i]]

        return max(res, key=len)  # return max length set