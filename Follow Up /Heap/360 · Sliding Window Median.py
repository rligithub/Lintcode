import heapq


class Solution:
    # stream data median == add num + find median
    # sliding window median == add num until len == k, find median, delete num add num, find next median
    # use hashmap to save nums in heap
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """

    def medianSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []
        maxheap = []
        minheap = []
        res = []

        for i in range(len(nums)):
            if len(maxheap) + len(minheap) < k:
                self.add(nums[i], maxheap, minheap)

            if len(maxheap) + len(minheap) == k:
                res.append(-maxheap[0])
                self.delete(nums[i + 1 - k], minheap, maxheap)
        return res

    def add(self, num, maxheap, minheap):
        val = heapq.heappushpop(maxheap, - num)
        heapq.heappush(minheap, - val)
        if len(minheap) > len(maxheap):
            heapq.heappush(maxheap, - heapq.heappop(minheap))

    def delete(self, num, minheap, maxheap):
        if num in minheap:
            minheap.remove(num)
            if len(minheap) < len(maxheap) - 1:
                heapq.heappush(minheap, - heapq.heappop(maxheap))
        elif -num in maxheap:
            maxheap.remove(-num)
            if len(minheap) > len(maxheap):
                heapq.heappush(maxheap, - heapq.heappop(minheap))

import bisect
class Solution1: # use bisect to sort window
    def medianSlidingWindow(self, nums, k):
        res = []
        window = sorted(nums[:k])
        res.append(self.median(window, k))
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            bisect.insort(window, nums[i])
            res.append(self.median(window, k))
        return res

