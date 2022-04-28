class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        if len(nums) == 0:
            return []
        j = 0
        for i in range(len(nums)):
            j = max(j,i + 1) # to make sure j is always after i
            while j < len(nums) and nums[j] - nums[i] < abs(target):
                j += 1

            if j >= len(nums):
                break
            if nums[j] - nums[i] == abs(target):
                return [nums[i], nums[j]]



nums = [1,2,4]
target = 4
a = Solution()
print(a.twoSum7(nums, target))