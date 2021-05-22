print('60 · Search Insert Position')

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if len(A) ==0:
            return  0
        if target <A[0]:
            return  0
        if target > A[-1]:
            return len(A)

        start, end =0, len(A)-1
        while start + 1 < end:
            mid = (end - start) //2 + start
            if target <= A[mid]:
                end = mid
            else:
                start = mid
        if target <= A[start]:
            return start
        if target <= A[end]:
            return end

data = [1,10,201,1001,10001,10007]
target = 10008
a=Solution()
print(a.searchInsert(data,target))