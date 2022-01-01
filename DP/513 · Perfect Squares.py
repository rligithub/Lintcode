class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        dp = [n] *(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i],dp[i-j*j] +1)
                j += 1
        return dp[-1]

n= 13
a = Solution()
print(a.numSquares(n))