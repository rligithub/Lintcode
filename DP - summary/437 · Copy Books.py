class Solution: # binary search
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if not pages or k == 0:
            return 0
            # 最短时间取决于 最慢的人的时间, 最长时间 等于 一个人复印所有书的时间
        left, right = max(pages), sum(pages)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.peopleneeded(pages, mid) > k:  # more people, less time -- > need more time --> increase timespent
                left = mid
            else:
                right = mid
        if self.peopleneeded(pages, left) <= k:
            return left
        if self.peopleneeded(pages, right) <= k:
            return right

    def peopleneeded(self, pages, timespend):
        total = 0
        people = 0
        for page in pages:
            if total + page > timespend:
                people += 1
                total = 0
            total += page
        return people + 1


class Solution: # dp --> TLE
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if not pages:
            return 0
        if not k:
            return float('inf')

        n = len(pages)
        # dp[k][i] --> max pages or time that k people spend to copy i books
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(1, n + 1):
            dp[0][i] = float('inf')

        # i -- > num of book in total
        # k --> people
        # j --> num of book copied by k-1 people
        for p in range(1, k + 1):
            dp[p][0] = 0
            for i in range(1, n + 1):
                dp[p][i] = float('inf')
                total_pages = 0
                # kth people need to copy {j... i-1} book
                # then, compare it to max time spend for k-1 people
                for j in range(i, -1, -1):
                    dp[p][i] = min(dp[p][i], max(dp[p - 1][j], total_pages))
                    if j > 0:
                        total_pages += pages[j - 1] # j ==> 0------j-------- i-1  from right to left, totalpages += pages[j]
        return dp[-1][-1]


