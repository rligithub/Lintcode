class Solution:
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

