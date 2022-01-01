class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        if not L:
            return 0

        left, right = 1, max(L)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.getpieces(L, mid) < k:
                right = mid
            else:
                left = mid
                # to find the first position, need to check right index first
        if self.getpieces(L, right) >= k:
            return right

        if self.getpieces(L, left) >= k:
            return left
        return 0

    def getpieces(self, L, length):
        res = 0
        for num in L:
            res += num // length
        return res
