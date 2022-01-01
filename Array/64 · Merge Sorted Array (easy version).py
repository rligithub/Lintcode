class Solution: # add array B to array A with sorted order
    # compare A[i] and B[j] from the end
    # use new index k from to copy and paste larger of A[i] or B[j]

    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        if n == 0:
            return
        #resize A
        for i in range(n):
            A.append(0)

        i = m-1
        j = n-1
        k = m+n-1 #new index
        while i >= 0 and j >=0:
            if A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1
            k -= 1
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1

A = [1,2,5]
m = 3
B = [3,4]
n = 2
a = Solution()
print(a.mergeSortedArray(A,m,B,n))
print(A)
