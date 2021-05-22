print('First Bad Version')

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        start, end = 1, n
        while start + 1 < end:
            mid = (end - start) //2 + start
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end

n=5
a=Solution()
print(a.findFirstBadVersion(n))