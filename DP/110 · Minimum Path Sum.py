class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if not grid:
            return
        res = [[0 for i in range(len(row))] for row in grid]
        res[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # consider two corner cases: i == 0 and j ==0
                if i ==0:
                    res[i][j] = grid[i][j] + res[i][j-1]
                elif j == 0:
                    res[i][j] = grid[i][j] + res[i-1][j]
                else:
                    res[i][j] = grid[i][j] + min(res[i-1][j],res[i][j-1])
        return res[-1][-1]
