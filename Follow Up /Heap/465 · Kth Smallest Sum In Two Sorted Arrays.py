import heapq


class Solution:  # brute force
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """

    def kthSmallestSum(self, A, B, k):
        if not A and not B or k == 0:
            return 0

        res = []
        for num1 in A:
            for num2 in B:
                total = num1 + num2
                heapq.heappush(res, total)

        for i in range(k - 1):
            heapq.heappop(res)
        return heapq.heappop(res)


