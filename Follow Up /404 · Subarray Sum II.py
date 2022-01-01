class Solution: # LTE
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        if not A:
            return 0
        n = len(A)
        dp = [0] *(n+1)
        count = 0
        for i in range(1,n+1):
            dp[i] = dp[i-1] + A[i-1]
            for j in range(i):
                if start <= dp[i] - dp[j] <= end:
                    count += 1
        return count
