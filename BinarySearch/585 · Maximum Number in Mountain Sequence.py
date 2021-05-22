print('585 · Maximum Number in Mountain Sequence')


def mountainSequence(self, nums):
    start, end =0, len(nums)-1
    while start + 1 < end:
        mid = (end - start) //2 + start
        if nums[mid] > nums[mid+1]:
            end = mid
        elif nums[mid] < nums[mid+1]:
            start = mid
        else:
            end = mid
    return max(nums[start],nums[end])




nums = [1, 2, 50, 8, 6, 3]
print(mountainSequence(0,nums))