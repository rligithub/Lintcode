class Solution:
    # use DP to 压扁 2D matrix to 1D --> convert to largest rectangle in histogram problem
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

            # use DP to 压扁 --> DP is a histogram now
        # 每压缩一层，算一次res (includes above height), since res can only be positive, accumlated res
        n = len(matrix[0])
        height = [0] * (n + 1)
        res = 0
        for row in matrix:
            for i in range(n):
                if row[i] == 1:
                    height[i] += 1
                else:
                    height[i] = 0  # 一旦中间是个零，间断reset，重新计算高度
            stack = [-1]  # reset stack for each row

            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    res = max(res, h * w)
                stack.append(i)
        return res




