class Solution1:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):

        if not costs:
            return 0

        # n --> house ; k --> color
        n, k = len(costs), len(costs[0])

        dp = [[0] * (k) for _ in range(n + 1)]

        # base case
        for color in range(k):
            dp[0][color] = 0

        # dp[i][j] -- > the min cost to paint house i with color j
        # look at min cost to paint house i-1 with color k {j != k} --> dp[i-1][k]
        color1, color2 = 0, 0
        for i in range(1, n + 1):
            min1 = min2 = float('inf')
            # maintain min1 and min2 in each level
            for j in range(k):
                if dp[i - 1][j] < min1:
                    min2 = min1
                    color2 = color1

                    min1 = dp[i - 1][j]
                    color1 = j
                else:
                    if dp[i - 1][j] < min2:
                        min2 = dp[i - 1][j]
                        color2 = j
            # compare color in house i to color in house i-1
            for j in range(k):

                if j != color1:
                    dp[i][j] += costs[i - 1][j] + min1
                else:
                    dp[i][j] += costs[i - 1][j] + min2

                    # res = min cost to paint nth house in difference colors

        res = min(dp[-1])

        return res


class Solution2: #TLE
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """

    def minCostII(self, costs):
        if not costs:
            return 0

        m, n = len(costs), len(costs[0])

        dp = [[0] * n for _ in range(m)]

        dp[0] = costs[0]
        for i in range(1, m):
            for j in range(n):
                temp = dp[i - 1][:j] + dp[i - 1][j + 1:]
                dp[i][j] = costs[i][j] + min(temp)
        return min(dp[-1])


