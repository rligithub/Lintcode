print('159 · Find Minimum in Rotated Sorted Array')

Data = [4, 5, 6, 7, 0, 1, 2]
#Output：0
#Explanation：
#The minimum value in an array is 0.


def findMin(self, nums):
    if not nums:
        return -1

    start= 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = (end - start) //2 + start
        if nums[mid] > nums[end]:
            start= mid
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid
    return min(nums[start],nums[end])

print(findMin(0,Data))