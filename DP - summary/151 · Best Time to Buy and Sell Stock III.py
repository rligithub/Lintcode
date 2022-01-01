class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if not prices:
            return 0

        buy1, buy2 = float('-inf'), float('-inf')
        sold1, sold2 = 0, 0

        for p in prices:
            buy1 = max(buy1, -p)
            sold1 = max(sold1, buy1 + p)
            buy2 = max(buy2, sold1 - p)
            sold2 = max(sold2, buy2 + p)
        return max(sold1, sold2)
