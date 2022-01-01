class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            if i > 1:
                j = 10 * int(s[i - 2]) + int(s[i - 1])
                if 10 <= j <= 26:
                    dp[i] += dp[i - 2]

        return dp[-1]
