class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """

    def maxProfit(self, K, prices):
        if not K or not prices:
            return 0

        n = len(prices)

        # SAME TO QUESTION II --> complated unlimited transactions 每天都有交易 -- >  买卖是一次transactions
        if K >= n // 2:
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

            # Completed k transactions
        dp = [[0] * n for _ in range(K + 1)]

        for i in range(1, K + 1):
            maxdiff = float('-inf')
            for j in range(1, n):
                # case 1 - sell today ==> price today - (price yesterday - maxprofit yesterday)
                # case 2 - not sell today
                maxdiff = max(maxdiff, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxdiff)
        return dp[-1][-1]


class Solution2: # dfs + memo
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """

    def maxProfit(self, K, prices):
        memo = {}
        return self.dfs(K, prices, 0, False, memo)

    def dfs(self, K, prices, pos, has_stock, memo):
        if (K, pos, has_stock) in memo:
            return memo[(K, pos, has_stock)]

        if pos > len(prices) - 1:
            return 0

            # case1 -> not action today
        no_action = self.dfs(K, prices, pos + 1, has_stock, memo)

        # case2 -> sell or buy today
        if has_stock:  # if has stock -- > sell
            action = self.dfs(K, prices, pos + 1, False, memo) + prices[pos]
        else:  # if no stock --> buy
            if K > 0:
                action = self.dfs(K - 1, prices, pos + 1, True, memo) - prices[pos]
            else:
                action = 0

        memo[(K, pos, has_stock)] = max(no_action, action)
        return memo[(K, pos, has_stock)]


a = Solution()
K = 1
prices = [3,4,8,5]

print(a.maxProfit(K, prices))