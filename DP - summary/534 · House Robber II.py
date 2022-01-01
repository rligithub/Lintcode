class Solution: # compressed dp 
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        n = len(nums)
        old = 0
        now = nums[0]
        for i in range(2, n + 1):
            temp = max(now, old + nums[i - 1])
            old = now
            now = temp
        return now


