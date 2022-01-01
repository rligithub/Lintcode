import collections


class Solution1: # use two sets
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums:
            return 0
        table = set()
        visited = set()
        count = 0


        for num in nums:
            if target - num in table and num not in visited:
                count += 1
                visited.add(num)
                visited.add(target - num)
            table.add(num)

        return count

import collections


class Solution2: # use two pointers
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if len(nums) == 0:
            return 0
        left, right = 0 , len(nums) -1
        count = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1


            elif nums[left] + nums[right] > target:
                right -= 1

            else:
                left += 1

        return count


nums = [1,1,2,45,46,46]
target = 47
a = Solution2()
print(a.twoSum6(nums, target))
