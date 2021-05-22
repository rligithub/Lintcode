print('437 · Copy Books')

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (end - start) //2 + start
            if self.people_need (pages, mid) > k:
                start = mid
            else:
                end = mid
        if self.people_need (pages, start) <=k:
            return start
        if self.people_need (pages, end) <=k:
            return end

    def people_need(self,pages, time):
        sum = 0
        count =0
        for page in pages:
            if sum + page > time:
                count +=1
                sum =0
            sum += page
        return count +1

pages = [3, 2, 4]
k = 3

a=Solution()
print(a.copyBooks(pages,k))


