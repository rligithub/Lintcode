print('447 · Search in a Big Sorted Array')

Data=[1,3,3,6,9,21]
#target = 3

def searchBigSortedArray(self, reader, target):
# find index kth for reader
# binary search the target between index 0 and index kth == logk
    kth = 1
    while reader[kth-1] < target:
        kth = 2*kth
    start = 0
    end = kth-1
    while start +1 < end:
        mid = (end - start) // 2 + start
        if (reader[mid] < target):
            start = mid
        else:
            end = mid
    if reader[start] == target:
        return start
    if reader[end] == target:
        return end
    return -1

print(searchBigSortedArray(0,Data,3))

