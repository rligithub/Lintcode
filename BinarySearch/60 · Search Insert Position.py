print('60 · Search Insert Position')

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def binary_search(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            # Use __lt__ to match the logic in list.sort() and in heapq
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    #
    # def searchInsert(self, A, target):
    #     if len(A) ==0:
    #         return  0
    #     if target <A[0]:
    #         return  0
    #     if target > A[-1]:
    #         return len(A)
    #
    #     start, end =0, len(A)-1
    #     while start + 1 < end:
    #         mid = (end - start) //2 + start
    #         if target <= A[mid]:
    #             end = mid
    #         else:
    #             start = mid
    #     if target <= A[start]:
    #         return start
    #     if target <= A[end]:
    #         return end

data = [1,10,201,1001,10001,10007]
target = 10002
a=Solution()
print(a.searchInsert(data,target))