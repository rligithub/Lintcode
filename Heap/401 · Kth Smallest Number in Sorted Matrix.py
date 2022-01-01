import heapq
class Solution1: # push all values into heap, then pop k times out
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        heap = []
        res = 0
        if m ==0 or n == 0:
            return []
        if m*n < k:
            return matrix
        for row in range(m):
            for col in range(n):
                heapq.heappush(heap,matrix[row][col])
        for i in range(k):
            res = heapq.heappop(heap)
        return res



matrix = [
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
k = 4
a = Solution1()
print(a.kthSmallest(matrix, k))