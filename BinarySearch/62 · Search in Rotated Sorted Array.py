print('62 · Search in Rotated Sorted Array')


def search(self, A, target):
    start, end =0, len(A)-1
    if len(A)==0:
        return -1
# compare start position to mid position, two cases
# then compare, if target is in the side(with ascending order)

    while start + 1 < end:
        mid = (end - start) //2 + start
        if A[mid] == target:
            return mid
        if A[mid] > A[start]:
            if A[start] <= target < A[mid]:
                end = mid
            else:
                start = mid
        else:
            if A[mid] < target <= A[end]:
                start = mid
            else:
                end = mid

    if target == A[start]:
        return start
    if target == A[end]:
        return end
    else:
        return -1


A = [4,5,6,7,9,1,2]
target = 4

print(search(0,A, target))