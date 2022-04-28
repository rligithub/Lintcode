class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        res =[]
        if len(s) == 0:
            return res
        self.dfs(s, res, [], 1)
        return res

    def dfs(self,s , res, path, index):
        if index == len(s) + 1:
            res.append(path)
            return

        for i in range(index, len(s)+1):
            if self.isPartition(s[index-1:i]):
                self.dfs(s, res, path + [s[index-1:i]], i+1)

    def isPartition(self,s):
        return s == s[::-1]


class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        res =[]
        if len(s) == 0:
            return res
        self.dfs(s, res, [], 0)
        return res

    def dfs(self,s , res, path, index):
        if index == len(s):
            res.append(path)
            return

        for i in range(index, len(s)):
            if self.isPartition(s[index:i+1]):
                self.dfs(s, res, path + [s[index:i+1]], i+1)

    def isPartition(self,s):
        return s == s[::-1]


s = "aab"

a = Solution()
print(a.partition(s))
