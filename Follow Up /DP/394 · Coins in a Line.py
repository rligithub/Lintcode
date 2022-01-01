class Solution1:
    def firstWillWin(self, n):
        # write your code here
        print(n)
        if n == 0:
            return False
        if n <= 2:
            return True

        if self.firstWillWin(n - 1) == False or self.firstWillWin(n - 2) == False:
            return True
        return False


class Solution2:
    def __init__(self):
        self.memo = {}

    def firstWillWin(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 0:
            return False
        if n <= 2:
            return True

        if self.firstWillWin(n - 1) == False or self.firstWillWin(n - 2) == False:
            self.memo[n] = True
            return True
        self.memo[n] = False
        return False


class Solution:
    def firstWillWin(self, n):
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        print(n)
        if n in memo:
            return memo[n]

        if n == 0:
            return False
        if n <= 2:
            return True

        if self.dfs(n - 1, memo) == False or self.dfs(n - 2, memo) == False:
            memo[n] = True
            return True
        memo[n] = False
        return False


n = 4
a = Solution()
print(a.firstWillWin(n))