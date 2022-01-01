import collections


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        heap = []
        res = []
        for point in points:
            dis_sq = (point.x - origin.x)**2 + (point.y - origin.y)**2
            heapq.heappush(heap, (dis_sq, point.x, point.y))

        for i in range(k):
            dis, x, y = heapq.heappop(heap)
            res.append(Point(x,y))

        return res


# points = [[4,6],[4,7],[4,4],[2,5],[1,1]]
points = [Point(4, 6),Point(4, 7),Point(4, 4),Point(2, 5),Point(1, 1)]
origin = Point(0, 0)
k = 3
a = Solution()
print(a.kClosest(points,origin,k))