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
        print(envelopes)
        for envelope in envelopes:
            height = envelope[1]

            # add y value, if x > last value (height) saved in result
            if len(result) == 0 or height > result[-1]:
                result.append(height)
            else:
                # find the most left index to replace smaller y value in results. make sure y value in result is 越小越好
                index = self.binary_search(result, height)

                result[index] = height

        return len(result)

    def binary_search(self, A, target):
        if not A:
            return 0
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target > A[mid]:
                left = mid
            else:
                right = mid
        if target >= A[left]:
            return left
        if target >= A[right]:
            return right

result = [2,2,3,3,5]
height = 2.5
index = bisect.bisect_right(result, height)

print(index)

a = Solution()
envelopes = [[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]]
print(a.maxEnvelopes(envelopes))