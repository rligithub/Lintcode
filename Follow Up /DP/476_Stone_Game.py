class Solution:
    def stoneGame(self, A):
        if not A:
            return 0
        memo = {}
        self.presum = [0]
        for num in A:
            self.presum.append(self.presum[-1] + num)
        return self.dfs(A, 0, len(A) - 1, memo)

    def dfs(self, A, start, end, memo):
        print(start, end)
        if (start, end) in memo:
            return memo[(start, end)]

        if start >= end:
            return 0

        cost = self.presum[end + 1] - self.presum[start]
        res = float('inf')
        for mid in range(start, end):
            left = self.dfs(A, start, mid, memo)
            right = self.dfs(A, mid + 1, end, memo)
            res = min(res, left + right + cost)

        memo[(start, end)] = res
        return res


nums = [4, 1, 1, 4]
a = Solution()
print(a.stoneGame(nums))

