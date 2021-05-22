print('61 · Search for a Range')

def searchRange(self, A, target):

# find the first then find the last position of the target value
    if len(A) ==0:
        return [-1,-1]
    start,end =0, len(A)-1
    while start +1 < end:
        mid = (end + start) // 2
        if target > A[mid]:
            start = mid
        elif target < A[mid]:
            end = mid
        else:
            end = mid
    if A[start] == target:
        left =start
    elif A[end] == target:
        left =end
    else:
        return [-1,-1]
    start, end = left, len(A)-1
    while start + 1 < end:
        mid = (end + start) //2
        if target > A[mid]:
            start = mid
        elif target < A[mid]:
            end = mid
        else:
            start = mid
    if A[end] == target:
        right =end
    else:
        right = start


    return [left, right]

A = [5, 7, 7, 8, 8, 10]
target = 8

print(searchRange(0,A,target))





