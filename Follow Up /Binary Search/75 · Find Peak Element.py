class Solution: # Brace force
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        if len(A) < 3:
            return
        for i in range(2,len(A)):
            if A[i-2] < A[i-1] and A[i-1] > A[i]:
                return i-1


class Solution2:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # binary search --> find mid --> find mid
        # if A[mid] > A[mid+1] --> go left side --> right = mid
        # if A[mid] < A[mid+1] --> go right side --> left = mid
        if len(A) < 3:
            return
        left, right = 0, len(A) - 1

        # stop when left and right is next to each other
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid
        # get higher values
        if A[left] > A[right]:
            return left
        else:
            return right
