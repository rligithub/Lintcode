class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # use two pointers from left to right, copy non-zero value to replace zero value
        if not nums:
            return
        fast, slow = 0, 0
        while fast < len(nums) and slow < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        return nums
nums = [0, 0, 0, 3, 1]
a = Solution()
print(a.moveZeroes(nums))

