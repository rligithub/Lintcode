class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # 两种情况，case1: 正正得正 ; case2:负负得正
        # if last num at index i is positive, need to get maxproduct at index i-1
        # if last num at index i is negative, need to get minproduct at index i-1

        # corner case
        if not nums:
            return 0

        res = float('-inf')
        # create two dp
        maxdp = [0] * len(nums)
        mindp = [0] * len(nums)

        for i in range(0, len(nums)):
            # base case
            maxdp[i] = nums[i]
            mindp[i] = nums[i]
            if i > 0:  # to compare value in prev index
                maxdp[i] = max(maxdp[i], max(maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i]))
                mindp[i] = min(mindp[i], min(mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i]))

            res = max(res, maxdp[i])  # mindp的作用只是用来比较maxdp（负负得正的情况下maxdp是多少）
        return res
