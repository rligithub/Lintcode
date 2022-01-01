import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        hea = [1]
        sex = [2,3,5]
        for i in range(n):
            x = heapq.heappop(hea)
            for j in range(3):
                if x * sex[j] not in hea:
                    heapq.heappush(hea, x*sex[j])
        return x

n = 9
a = Solution()
print(a.nthUglyNumber(n))