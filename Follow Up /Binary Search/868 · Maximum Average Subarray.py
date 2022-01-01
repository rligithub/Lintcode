class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """

    def findMaxAverage(self, nums, k):
        if not nums or k == 0:
            return 0
        numsum = 0
        maxsum = 0
        for i in range(k):
            numsum += nums[i]
            maxsum = max(maxsum, numsum)

        for i in range(k, len(nums)):
            numsum = numsum - nums[i - k] + nums[i]
            maxsum = max(maxsum, numsum)

        return maxsum / k


