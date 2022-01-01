class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        if not costs:
            return 0

            # house n ==> column
        n = len(costs)

        dp = [[float('inf')] * 3 for _ in range(n + 1)]

        # base case
        dp[0][0] = dp[0][1] = dp[0][2] = 0

        # i --> house ; j --> color of house i; k --> color of house i-1
        for i in range(1, n + 1):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])

        return min(dp[-1][0], dp[-1][1], dp[-1][2])
