class Solution1: # two pointer in opposite directions
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if len(nums) ==0:
            return []
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] % 2 == 1:
                left += 1
                continue
            if nums[right] %2 == 0:
                right -= 1
                continue
            if nums[left] % 2 == 0 and nums[right] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums

class Solution2: # two pointer in the same direction
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if len(nums) ==0:
            return []
        slow, fast = 0, 0
        while fast <= len(nums) -1:
            if nums[fast] %2 == 1:
                nums[slow], nums[fast] = nums[fast],nums[slow]
            if nums[slow] % 2 == 1:
                slow += 1
            fast += 1
        return nums


nums = [1,4,2,3,5,7]
a = Solution2()
print(a.partitionArray(nums))






