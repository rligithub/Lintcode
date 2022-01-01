class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return A[0]
        dp = [0] * len(A)

        # compare incl current home to excl current home
        # incl = dp[i-2] + A[i]
        # excl = dp[i-1]

        dp[0] = A[0]

        dp[1] = max(dp[0], A[1])

        res = dp[1]
        for i in range(2, len(A)):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i])
            res = max(res, dp[i])
        return res



