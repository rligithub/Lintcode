import collections


class Solution:
    # save each stone position and steps to jump to each stone in a dict
    # bp[0] = {0}
    # bp[i] = current steps used to get to stone i
    # next stone --> bp[i + jumped] = jumped ; jumped is within [currentStep + 1, currentStep -1, currentStep]

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
            for k in bp[stone]: # k represents total steps that we can jumped to stone
                for jumped in [k -1 , k, k+1]:
                    if jumped > 0 and stone + jumped in bp:
                        bp[stone + jumped].add(jumped) # save total steps used to jump to next stone
        return len(bp[stones[-1]]) > 0

stones = [0,1,3,5,6,8,12,17]
a = Solution()
print(a.canCross(stones))
