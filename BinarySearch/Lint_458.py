print('458. Last position of Target')

nums = [1,2,2,4,5,5]
#target = 5
#answer = 2
def lastPosition(self, nums, target):
    if not nums or target is None:
        return -1
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (end - start) // 2 + start
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            start = mid #to find last position, include mid position in left
    if nums[end] == target:
        return end
    elif nums[start] == target:
        return start
    else:
        return -1

print(lastPosition(0,nums,5))