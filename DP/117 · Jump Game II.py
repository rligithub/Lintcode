class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        dp = [0] * len(A)
        for i in range(len(A)):
            for j in range(1, A[i] + 1):
                jumped = i + j
                if jumped < len(A):  # if jumped > len(A), return 0
                    if dp[jumped] == 0:
                        dp[jumped] = dp[i] + 1
                        if jumped == len(A) - 1:
                            return dp[-1]

        return 0






