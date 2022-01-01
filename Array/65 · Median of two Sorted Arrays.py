class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # Time complexity is O(log(m+n)) --> use binary search
        # compare mid index of A and mid index of B
        # if A[mid] < B[mid] ==> median is not in range B[0:mid], find mid of A[mid+1:] and B

        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findmid(A, B, l // 2)
        else:
            return (self.findmid(A, B, l // 2) + self.findmid(A, B, l // 2 - 1)) / 2

    def findmid(self, A, B, k):
        if not A:
            return B[k]
        if not B:
            return A[k]
        i, j = len(A) // 2, len(B) // 2

        if i + j < k:
            if A[i] < B[j]:
                return self.findmid(A[i + 1:], B, k - i - 1)
            else:
                return self.findmid(A, B[j + 1:], k - j - 1)
        else:
            if A[i] < B[j]:
                return self.findmid(A, B[:j], k)
            else:
                return self.findmid(A[:i], B, k)


A = [1,2,3,4,5,6]
B = [2,3,4,5]
a = Solution()
print(a.findMedianSortedArrays(A,B))


