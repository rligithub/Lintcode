class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        if not A:
            return True

        # dp[j] --> whether or not can reach to index j
        # i --> last second index
        # check if can get to dp[i] and i + A[i] >= j ---> dp[j] = True
        n = len(A)
        dp = [0] * n
        print(dp)
        # dp base case
        dp[0] = True
        for j in range(1, n):
            dp[j] = False
            for i in range(0, j):  # 看是否能从i跳到j
                if dp[i] and i + A[i] >= j:
                    dp[j] = True
                    break
        return dp[-1]


class Solution2: # update DP[i] as global max index that we can jump to, compare dp[i] to last index(n-1)
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

class Solution3: # keep a global variable
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

