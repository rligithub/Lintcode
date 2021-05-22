print('14. First position of Target')

tuple = [1,4,4,5,7,7,8,9,9,10]

#target = 1
#answer = 0

def binarySearch(self, nums, target):
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (end - start) // 2 + start
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            end = mid #to find first position, include mid position in right
    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    else:
        return -1

print(binarySearch(0,tuple,1))