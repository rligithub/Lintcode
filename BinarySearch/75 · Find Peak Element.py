print('75 · Find Peak Element')

def findPeak(self, A):
    start,end =0, len(A)-1

    while start + 1 < end:
        mid = (end - start) //2 + start
        if A[mid-1] > A[mid] > A[mid+1]:
            end = mid
        elif A[mid] < A[mid+1]:
            start = mid
        else:
            end = mid
    if A[start]>A[end]:
        return start
    else:
        return end




A = [1, 2, 7, 4, 1]
print(findPeak(0,A))