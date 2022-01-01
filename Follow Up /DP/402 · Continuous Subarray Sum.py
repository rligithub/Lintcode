class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySum(self, A):
        if not A:
            return []

        dp = [0] * len(A)
        dp[0] = A[0]
        end = 0
        for i in range(1, len(A)):
            dp[i] = max(dp[i - 1] + A[i], A[i])
        globalmax = max(dp)
        end = dp.index(globalmax)
        total = sum(A[:end+1])
        start = 0
        for i in range(end+1):
            if total == globalmax:
                start = i
                break
            total -= A[i]
        return [start, end]

class Solution2:#贪心
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        cursum, minsum =0,0
        maxsum = float('-inf')

        l, r = -1, -1
        minpos = -1

        for i, num in enumerate(A):
            cursum += num
            if cursum - minsum > maxsum:
                maxsum = cursum - minsum
                l, r = minpos +1, i
            if cursum < minsum:
                minsum = cursum
                minpos = i
        return [l, r]

A = [-2,0,0,1,-1,-1]
a = Solution()
print(a.continuousSubarraySum(A))













