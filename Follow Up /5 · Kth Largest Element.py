import heapq


class Solution1:  #heap
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, nums):
        if len(nums) < k:
            return
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


import random


class Solution:  # quickselection
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, nums):
        if len(nums) < k:
            return

        return self.quickselection(nums, 0, len(nums) - 1, k)

    def quickselection(self, nums, left, right, k):

        pos = self.partition(nums, left, right)

        if pos == k - 1:
            return nums[pos]
        if pos > k - 1:
            return self.quickselection(nums, left, pos - 1, k)
        else:
            return self.quickselection(nums, pos + 1, right, k)


    def partition(self, nums, left, right):

        index = random.randint(left, right)
        nums[index], nums[right] = nums[right], nums[index]

        slow = left
        for fast in range(left, right):
            if nums[fast] > nums[right]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        nums[slow], nums[right] = nums[right], nums[slow]
        return slow


k = 1
nums = [1,3,4,2]

a = Solution()
print(a.kthLargestElement(k, nums))