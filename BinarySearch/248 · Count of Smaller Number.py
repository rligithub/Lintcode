import bisect

class Solution:
    def countOfSmallerNumber(self, A, queries):
       res=[]
       A.sort()
       for num in queries:
           res.append(self.Binary_search(A,num))
       return res

    def Binary_search(self,A,num):
        if not A:
            return 0
        start, end =0, len(A)-1
        while start + 1 < end:
            mid = (end - start) //2 + start
            if num > A[mid]:
                start = mid
            else:
                end = mid

        if num <= A[start]:
            return start
        if num <= A[end]:
            return end
        return end +1







A = [1,2,3,4,5,6]
queries = [1,2,3,4]
a = Solution()
print(a.countOfSmallerNumber(A, queries))


