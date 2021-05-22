print('462 · Total Occurrence of Target')

def totalOccurrence(self, A, target):
# find the first position and last position, then get the index difference

    if len(A) ==0:
        return 0
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
        return 0
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


    count= right-left +1
    return count

A= [1, 3, 3,3, 4, 5]
target = 3

print(totalOccurrence(0,A,target))