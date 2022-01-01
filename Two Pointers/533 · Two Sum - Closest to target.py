import collections


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        if len(nums) == 0:
            return 0
        nums.sort()
        left, right = 0, len(nums) -1
        diff = float('inf')
        while left < right:
            total = nums[left] + nums[right]
            diff = min(diff, abs(target - total))
            if total == target:
                diff = 0
                break
            elif total > target:
                right -= 1
            else:
                left += 1
        return diff


nums = [-1,2,1,-4]
target = 4
a = Solution()
print(a.twoSumClosest(nums, target))