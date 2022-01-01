import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        if not nums:
            return []
        if len(nums) < k:
            return nums
        heap = []
        res = []
        for num in nums:
            heapq.heappush(heap,-num)
        for i in range(k):
            res.append(-heapq.heappop(heap))
        return res

nums = [3, 10, 1000, -99, 4, 100]
k = 3
a = Solution()
print(a.topk(nums, k))