import collections


class Solution1:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """

    def canCross(self, stones):
        # use bp to save the steps used to get to each stone
        bp = collections.defaultdict(set)
        for stone in stones:
            bp[stone] = set()
        bp[0] = {0}

        for stone in stones:
            for k in bp[stone]:
                for jumped in [k - 1, k, k + 1]:
                    if jumped > 0 and stone + jumped in bp:
                        bp[stone + jumped].add(jumped)
        return len(bp[stones[-1]]) > 0


class Solution:  # top down dp
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """

    def canCross(self, stones):
        target = stones[-1]
        # convert to hashset --> find target in O(1) time complexity
        stones = set(stones)

        memo = {}
        return self.dfs(stones, 0, 1, target, memo)

    def dfs(self, stones, pos, steps, target, memo):
        if (pos, steps) in memo:
            return memo[(pos, steps)]

        if pos == target:
            return True

        for nextjump in (steps - 1, steps, steps + 1):
            if pos + nextjump in stones and nextjump != 0:
                if self.dfs(stones, pos + nextjump, nextjump, target, memo):
                    memo[(pos, steps)] = True
                    return True
        memo[(pos, steps)] = False
        return False


