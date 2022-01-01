class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0

        return max(self.increasingsubsequence(A), self.increasingsubsequence(A[::-1]))

    def increasingsubsequence(self, A):
        dp = [1] * len(A)
        res = 1

        # dp[i] -- > longest increasing subsequence in current index i
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                dp[i] = dp[i - 1] + 1
                res = max(res, dp[i])  # if last num is less than i-1, dp[i] is not max num then
        return res
