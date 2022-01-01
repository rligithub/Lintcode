class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # heapify -> find last child's parent
        # shift down
        if not A:
            return []
        for i in reversed(range(len(A)//2)):
            self.siftdown(A,i)

    def siftdown(self, A, i):
        n = len(A)
        while i * 2 + 1 < n:
            left = i *2 +1
            right = i* 2 +2
            if right < n and A[left] > A[right]:
                left += 1
            if A[left] >= A[i]:
                break
            A[i],A[left] = A[left], A[i]
            i = left


A = [3,2,1,4,5]
a = Solution()
print(a.heapify(A))
a.heapify(A)
print(A)