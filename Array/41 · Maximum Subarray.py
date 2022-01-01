class Solution: #DP - return max sum of subarray
    # compare  [sum of prev sum + current value] vs [current value]

    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        DP =[0] * n
        DP[0] = nums[0]

        for i in range(1,n):
            DP[i] = max(DP[i-1] + nums[i], nums[i])

        return max(DP)

nums = [-2,2,-3,4,-1,2,1,-5,3]
a = Solution()

print(a.maxSubArray(nums))