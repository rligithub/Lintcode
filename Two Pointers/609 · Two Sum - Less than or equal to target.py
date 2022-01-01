class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        left, right = 0, n -1
        count = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1

        return count

nums = [2, 7, 11, 15]
target = 24
a =Solution()
print(a.twoSum5(nums, target))

