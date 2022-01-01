import heapq


class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """

    def trapRainWater(self, heights):
        # use min-heap + BFS
        # 农村包围城市
        # 把所有外围的height放到heap里，pop到最小值，维持一个maxheight
        # 检查pop的值的四周，把周围的值放入heap里
        # if height[i][j] >= maxheight --> do nothing, can't trap water
        # if height[i][j] < maxheight --> calculate water = maxheight - height[i][j]

        if not heights:
            return 0
        m, n = len(heights), len(heights[0])
        heap = []
        res = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heights[i][j], i, j))
                    heights[i][j] = -1  # mark visited

        maxheight = float('-inf')

        while heap:
            cur, i, j = heapq.heappop(heap)
            maxheight = max(maxheight, cur)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and heights[x][y] != -1:
                    if heights[x][y] < maxheight:
                        res += maxheight - heights[x][y]
                    heapq.heappush(heap, (heights[x][y], x, y))
                    heights[x][y] = -1
        return res




