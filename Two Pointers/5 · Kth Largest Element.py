import random


class Solution: # use quick selection to sort the array, return nums[k-1]
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        return self.quickselect(nums, 0, len(nums) - 1, k)

    def quickselect(self, nums, left, right, k):
        pivot = self.partition(nums, left, right)
        if pivot == k - 1:
            return nums[pivot]
        elif pivot < k -1:
            return self.quickselect(nums, pivot + 1, right, k)  # left and right are index, k is also index #.
        else:
            return self.quickselect(nums, left, pivot - 1, k)

    def partition(self, nums, left, right):
        if len(nums) == 0:
            return 0
        # randomly select a num from array, swap it to last index
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]

        # use two pointers for same direction, make sure number bigger than pivot is always in left side of slow pointer
        slow = left
        for fast in range(left, right):
            if nums[fast] > nums[right]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        nums[slow], nums[right] = nums[right], nums[slow]
        return slow

k = 3
nums = [2,9,7,8,4,2]

a = Solution()
print(a.kthLargestElement(k, nums))