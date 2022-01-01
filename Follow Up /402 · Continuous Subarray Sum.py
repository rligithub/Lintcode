class Solution: #LTE
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        if not A:
            return []

        globalmax = float('-inf')

        for left in range(len(A)):
            right = left
            presum = 0
            while right < len(A):
                presum += A[right]
                if presum > globalmax:
                    globalmax = presum
                    l, r = left, right
                right += 1
        return [l, r]





