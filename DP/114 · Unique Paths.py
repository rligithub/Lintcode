class Solution1:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]

class Solution2:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        if m == 0 or n ==0:
            return 0
        res = [0 for j in range(m)]
        res[0] = 1
        for i in range(n):
            for j in range(1, m): #should start from index 1, not update res[0], otherwise res[j-1] would be res[-1]
                res[j] = res[j] + res[j-1]
        return res[-1]

n = 3
m = 1
a = Solution2()
print(a.uniquePaths(m,n))