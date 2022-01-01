class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        # maintain global min as day i, maxprofit[i] = price[i] - globalmin
        # maxprofit --> max(maxprofit[i])

        minP = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minP)
            minP = min(minP, prices[i])
        return res 