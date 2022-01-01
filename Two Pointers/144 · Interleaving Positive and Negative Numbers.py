class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        if len(A) == 0:
            return []

        # put all negative number in left and positive number in right
        left, right = 0, len(A)-1
        while left <= right:
            if A[left] < 0:
                left += 1
                continue
            if A[right] >=0:
                right -= 1
                continue
            if A[left] >=0 and A[right]<0:
                A[left], A[right] = A[right],A[left]
                left += 1
                right -= 1

        # check if [ # of negative number > # of positive number ]
        negatives = left
        positives = len(A) - left
        if negatives <= positives:
            l,r = 0,right + 1
        else:
            l,r = 1, right +1
        while r < len(A):
            A[l], A[r] = A[r], A[l]
            l += 2
            r += 1
        return A



A = [-33,-19,30,26,21,-9, 20]
a = Solution()
print(a.rerange(A))
