class Solution: # top down dp
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    def kSum(self, A, k, target):
        memo = {}
        return self.dfs(A, k, target, 0, memo)

    def dfs(self, A, k, target, pos, memo):
        if (target, k, pos) in memo:
            return memo[(target, k, pos)]

        if target == 0 and k == 0:
            return 1

        if pos > len(A) - 1:
            return 0

        pick = 0
        if k - 1 >= 0 and target - A[pos] >= 0:
            pick = self.dfs(A, k - 1, target - A[pos], pos + 1, memo)
        not_pick = self.dfs(A, k, target, pos + 1, memo)
        memo[(target, k, pos)] = pick + not_pick

        return memo[(target, k, pos)]
