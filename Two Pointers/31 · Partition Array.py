class Solution: # make sure [value < k] is in left side and [value > k] is in right side
        # use two pointers for opposite direction, return index after partition
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        n = len(nums)
        if n < k:
            return n

        i, j = 0, n -1
        while i <= j:
            if nums[i] < k:
                i += 1
                continue
            if nums[j] >= k:
                j -= 1
                continue
            if nums[i] >= k and nums[j] < k:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return i



nums = [1,2,3,4,1,1]
k = 2
a = Solution()
print(a.partitionArray(nums, k))
