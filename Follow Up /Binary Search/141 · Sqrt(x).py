class Solution1: # for loop
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 0 or x == 1:
            return x
        for num in range(1,x+1):
            if num * num > x:
                break
        return num - 1 #return prev num

class Solution2: #Binary search
    def sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
