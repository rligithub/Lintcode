class Solution: # keep a global variable
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        if not A:
            return True
        res = [0] * len(A)
        maxcount = float('-inf')
        for i in range(len(A)):
            res[i] = i + A[i]
            maxcount = max(maxcount, res[i])
            if res[i] >= len(A) - 1:
                return True
            if res[i] < i + 1 and maxcount < i + 1:
                return False

class Solution2: # update DP[i] as global max value
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, nums):
       n = len(nums)
       dp = [0] * n
       dp[0] = nums[0]
       for i in range(1, n):
           if i > dp[i-1]:
               return False
           dp[i] = i + nums[i]
           dp[i] = max(dp[i], dp[i-1])
           if dp[i] > n - 1:
               return True
       return dp[-1] >= n - 1