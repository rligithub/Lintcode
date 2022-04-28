import heapq
import random
from random import randint


class SolutionHeap1:
   def kthSmallest(self, k, nums):
        heapq.heapify(nums)

        for i in range(k - 1):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class SolutionHeap2:
    def kthSmallest(self, k, nums):

        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappush(heap, nums[i])

        for i in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)

import math

import math
class Solution3: # use quick selection
    """
    @param k: An integer
    @param nums: An integer arrayclass Solution: # count how many same color for each color, then replace colors[i] for each colors
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        n = len(colors)
        nums = [0] * (k+1)

        for num in colors:
            nums[num] += 1
        i = 0
        for color, count in enumerate(nums):
            while count > 0:
                colors[i] = color
                i += 1
                count -= 1
        return colors
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.quickselect(nums, 0, len(nums) -1, k)

    def quickselect(self, nums, left, right, k):
        pivot = self.partition(nums, left, right)
        if pivot == k -1:
            return nums[pivot]
        elif pivot < k -1:
            return self.quickselect(nums, pivot + 1, right, k)
        else:
            return self.quickselect(nums, left, pivot - 1, k)

    def partition(self, nums, left, right):
        if len(nums) == 0:
            return 0
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]

        slow = left
        for fast in range(left, right):
            if nums[fast] < nums[right]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
        nums[slow], nums[right] = nums[right], nums[slow]
        return slow


nums = [3, 4, 1, 2, 5]
k = 3
a = Solution3()

print(a.kthSmallest(k, nums))


