class Solution:  # top down dp
    """
    @param strs: an array with strings include only 0 and 1
    @param m: An integer
    @param n: An integer
    @return: find the maximum number of strings
    """

    def findMaxForm(self, strs, m, n):
        count = []
        for s in strs:
            count0 = 0
            count1 = 0
            for char in s:
                if char == "1":
                    count1 += 1
                if char == '0':
                    count0 += 1
            count.append([count0, count1])
        memo = {}
        return self.dfs(count, m, n, 0, memo)

    def dfs(self, table, m, n, pos, memo):
        if (m, n, pos) in memo:
            return memo[(m, n, pos)]
        if m == 0 and n == 0:
            return 0
        if pos > len(table) - 1:
            return 0

            # two cases
        pick = 0
        if m - table[pos][0] >= 0 and n - table[pos][1] >= 0:
            pick = self.dfs(table, m - table[pos][0], n - table[pos][1], pos + 1, memo) + 1
        not_pick = self.dfs(table, m, n, pos + 1, memo)

        memo[(m, n, pos)] = max(pick, not_pick)
        return memo[(m, n, pos)]
