class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        for i in range(0, n + 1):
            if i < 3:
                dp[i] = i
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

