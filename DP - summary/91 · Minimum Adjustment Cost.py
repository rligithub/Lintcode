class Solution:  # top down dp
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """

    def MinAdjustmentCost(self, A, target):

        res = float('inf')
        memo = {}

        # index 0 --> adjustment range = {1 to 100}
        # index 1 --> adjustment range = (prev index +- target)
        # index i --> adjustment range = (A[i-1] +- target)
        for num in range(1, 101):
            res = min(res, self.dfs(A, target, 1, num, memo) + abs(num - A[0]))
        return res

    def dfs(self, A, target, pos, num, memo):
        if (pos, num) in memo:
            return memo[(pos, num)]

        if pos > len(A) - 1:
            return 0

        res = float('inf')
        # index > 2; adjustment range is 1<= num[index] +- target <=100
        for i in range(max(1, num - target), min(101, num + target + 1)):
            res = min(res, self.dfs(A, target, pos + 1, i, memo) + abs(i - A[pos]))
        memo[(pos, num)] = res
        return res




