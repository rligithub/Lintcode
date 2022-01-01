import bisect


class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):

        if not envelopes or len(envelopes) == 0:
            return 0
        # sort envelopes by x value
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        result = []

        for envelope in envelopes:
            height = envelope[1]
            # add y value, if x > last value (height) saved in result
            if len(result) == 0 or height > result[-1]:
                result.append(height)
            else:
                #  找最小的比target大的元素，replace
                #  find the most left index to replace smaller y value in results. make sure y value in result is 越小越好
                index = bisect.bisect_left(result, height)
                result[index] = height

        return len(result)



