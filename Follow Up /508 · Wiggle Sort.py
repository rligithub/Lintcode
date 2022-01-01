class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """

    # 3 6 2 1 2 4
    #     f
    #     s

    def wiggleSort(self, nums):
        if not nums:
            return []

        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

            elif i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums


nums = [1,1,1,1,2]
a = Solution()
print(a.wiggleSort(nums))
