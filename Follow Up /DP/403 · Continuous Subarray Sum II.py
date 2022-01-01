class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def continuousSubarraySumII(self, A):
        if not A:
            return []
        n = len(A)
        summ = sum(A)
        res1 = self.findmax(A, 1)
        res2 = self.findmax(A, -1)

        # 两种情况，1 - maxsum集中在两端中间，2 - maxsum分散在两端（minsum肯定在中间）
        # 比较 case1: maxsum 和 case2: maxsum = totalsum - minsum
        # if maxsum1 > totalsum - minsum2 ==> return index for maxsum1
        # else ==> return index for minsum2 (need to %n, since maxsum2 should be from r to l)

        # if r2 - l2 == n-1 means that minsum == totalsum; in this case, if maxsum = negative number, it will be less than 0 (totalsum - minsum), will return r2 and l2
        # -100, -200, -300, -10, -400
        # maxsum1 == -10, minsum == totalsum == -1010
        # should return [3,3] for maxsum1
        if res1[2] > summ + res2[2] or res2[1] - res2[0] == n - 1:
            return [res1[0], res1[1]]
        else:
            # xxxxxxooooxxx
            #       l  r
            # return [(r+1) % n , (l-1) % n ]
            return [(res2[1] + 1) % n, (res2[0] - 1) % n]

    def findmax(self, A, minus):
        cursum, minsum = 0, 0
        maxsum = float('-inf')

        l, r = -1, -1
        minpos = -1

        for i, num in enumerate(A):
            cursum += num * minus
            if cursum - minsum > maxsum:
                maxsum = cursum - minsum
                l, r = minpos + 1, i
            if cursum < minsum:
                minsum = cursum
                minpos = i
        return l, r, maxsum
