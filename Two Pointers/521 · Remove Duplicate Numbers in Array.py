class Solution1:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # use two pointer for the opposite direction if don't need to keep original order
        if len(nums) == 0:
            return 0
        set =[]
        i,j = 0, len(nums)-1
        while i <= j:
            if nums[i] not in set:
                set.append(nums[i])
                i += 1
            else:
                nums[i],nums[j]= nums[j],nums[i]
                j -= 1
        return i

class Solution2:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # use two pointer for the same direction
        if len(nums) == 0:
            return 0
        nums.sort()
        i,j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        return i +1     # i is index

nums = [1,3,1,4,4,2]
a = Solution2()
print(a.deduplication(nums))