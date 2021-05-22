print('39 · Recover Rotated Sorted Array')

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        nums.sort()
        return nums

array = [4,5,1,2,3]
a=Solution()
print(a.recoverRotatedSortedArray(array))