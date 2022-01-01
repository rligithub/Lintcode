import heapq
class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        if not arrays or k == 0:
            return
        heap = []
        for row in arrays:
            for num in row:
                heapq.heappush(heap, -num)
        for i in range(k - 1):
            heapq.heappop(heap)
        return - heapq.heappop(heap)



