class Solution:
    # dp[i] --> min # of coins

    # 每一个dp[i] 测试 使用当前哪一种coin + dp[i-coin]，比较出最小值
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        if amount == 0 or not coins:
            return 0
        coins.sort()
        # dp[i] = min # of coins used to get amount of i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1

