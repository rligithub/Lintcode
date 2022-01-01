class Solution: # return the minimum length of subarray, whose sum equal to target
    # sliding window
    # step1: right ++ to test all possible results (sum += nums[right])
    # steo2: right ++ to test all possible results (sum -= nums[left])
    # size of subarray = right - left
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, target):
        if not nums or target == 0:
            return -1
        n = len(nums)
        left, right = 0, 0
        total = 0
        count = float('inf')
        while right < n:
            while right < n and total < target:
                total += nums[right]
                right += 1

            while left < n and total >= target:
                count = min(count, right - left)
                total -= nums[left]
                left += 1

        if count == float('inf'):
            return -1
        else:
            return count




