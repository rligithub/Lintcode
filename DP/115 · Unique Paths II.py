class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return
        res = [[0 for j in range(len(row))] for row in obstacleGrid]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    res[i][j] = 1
                elif i ==0:
                    res[i][j] = res[i][j-1]
                elif j ==0:
                    res[i][j] = res[i-1][j]
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]

class Solution2:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return
        res = [0 for j in range(len(obstacleGrid[0]))]
        res[0] = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                res[0] = 0
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    res[j] = 0
                else:
                    res[j] = res[j] + res[j-1]
        return res[-1]