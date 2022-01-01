class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        dp = [0] * (num + 1)
        dp[0] = 0
        # 二进制 右移 来看新的这个数有几个1，加上最末尾的值
        for i in range(num+1):
            dp[i] = dp[i>>1] + i%2
        return dp
