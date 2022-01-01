class Solution1:  # regular DP
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = A[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
        return dp[-1]


class Solution:  # compressed DP --> Space complexity = O(1)
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]

        old = 0
        now = A[0]
        for i in range(2, n + 1):
            cur = max(now, old + A[i - 1])
            old = now
            now = cur
        return now


