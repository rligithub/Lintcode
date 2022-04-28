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


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        # house n ==> column
        n = len(costs)
        if n == 0:
            return 0
        dp = [[float('inf')] * 3 for _ in range(2)]

        # base case
        dp[0][0] = dp[0][1] = dp[0][2] = 0

        # i --> house ; j --> color of house i; k --> color of house i-1
        for i in range(1, n + 1):
            for j in range(3):
                dp[i % 2][j] = float('inf')
                for k in range(3):
                    if k != j and dp[(i - 1) % 2][k] + costs[i - 1][j] < dp[i % 2][j]:
                        dp[i % 2][j] = dp[(i - 1) % 2][k] + costs[i - 1][j]

        return min(dp[n % 2][0], dp[n % 2][1], dp[n % 2][2])
