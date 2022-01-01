class Solution1: # bottom-up dp
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        if n == 0:
            return False
        dp = [False] * (n + 1)
        dp[1] = True

        # dp[i] --> if first player can win when we have coins i
        # dp[i-1] --> previous player (second player) takes 1 coin, but he loses --> we win
        # dp[i-2] --> previous player (second player) takes 2 coin, but he loses --> we win
        for i in range(2, n + 1):
            dp[i] = not dp[i - 1] or not dp[i - 2]
        return dp[-1]


class Solution2: # top -down dp
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return False
        if n == 1:
            return True

        # if second player has chance to lose, we win ; otherwise, we lose
        if self.dfs(n - 1, memo) == False or self.dfs(n - 2, memo) == False:
            memo[n] = True
            return True
        memo[n] = False
        return False


class Solution2_2: # top down dp
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """

    def firstWillWin(self, n):
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return False
        if n == 1:
            return True

            # memo -- > if first player can win or not
        # first player is opposite to second player, if second player win, we lose; if they lose, we win
        memo[n] = not self.dfs(n - 1, memo) or not self.dfs(n - 2, memo)
        return memo[n]