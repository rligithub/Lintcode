#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        if n == 0:
            return -1
        left, right = 1, n
        while left +1 < right: # +1 to represent there is mid between left and right
            mid = left + (right - left)//2
            if SVNRepo.isBadVersion(mid):
                right = mid
            else:
                left = mid
        if SVNRepo.isBadVersion(left):
            return left
        if SVNRepo.isBadVersion(right):
            return right
        return -1