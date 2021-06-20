left, right = 0, len(arr) -1
def reverse_mergesort(arr, left, right):
    if right - left < 1:
        return

    mid = left + (right - left)//2
    left_mid = left + (right-left)//4
    right_mid = left + (right -left)*3//4

    reverse(arr,left_mid,mid)
    reverse(arr,mid+1, right_mid)
    reverse(arr,left_mid, right_mid)

    reverse_mergesort(arr,left,left+2*(left_mid-left))
    reverse_mergesort(arr,left+2*(left_mid-left)+1,right)


def reverse(a,l,r):
    while l < r:
        a[l],a[r]= a[r],a[l]
    return a
