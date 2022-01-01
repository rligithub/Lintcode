class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
       if len(num) == 0:
           return 0
       hashset = set(num)
       maxcount = 0

       for x in num:
           if x-1 not in hashset: #make sure there is no consecutives number beore x
               count = 1
               while x+1 in hashset:
                   count += 1
                   x = x+1
               maxcount = max(maxcount, count)
       return maxcount







num = [100, 4, 200, 1, 3, 2]
a = Solution()
print(a.longestConsecutive(num))
