class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        left, right = 0, x
        if right < 1:
            right =1
        while left + 1e-12 < right:
            mid = left + (right - left)/2
            if mid*mid > x:
                right = mid
            else:
                left = mid
        return left

x = 2
a = Solution()
print(a.sqrt(x))