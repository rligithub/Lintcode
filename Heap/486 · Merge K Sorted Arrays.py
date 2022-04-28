import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays): # for loop by col index, similar to zigzag
        if not arrays:
            return []
        res = []
        heap = []
        for nums in arrays:
            for num in nums:
                heapq.heappush(heap,num)
        while heap:
            res.append(heapq.heappop(heap))

        return res
arrays = [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
a = Solution()
print(a.mergekSortedArrays(arrays))