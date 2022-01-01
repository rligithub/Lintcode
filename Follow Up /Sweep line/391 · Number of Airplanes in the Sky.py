"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # 把start和end的时间都存起来，sort一下
        # for loop --> start就+1, end就-1
        # 记录一个max值
        if not airplanes:
            return 0
        timetrack = []
        for airplane in airplanes:
            timetrack.append((airplane.start, 1))  # start += 1
            timetrack.append((airplane.end, -1))  # end -= 1

        timetrack.sort()
        res = 0
        globalmax = float('-inf')
        for time, value in timetrack:
            res += value
            globalmax = max(globalmax, res)

        return globalmax


class Solution1:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # 把start和end的时间都存起来，sort一下
        # for loop --> start就+1, end就-1
        # 记录一个max值
        if not airplanes:
            return 0
        timetrack = []
        for airplane in airplanes:
            timetrack.append((airplane.start, 1))  # start += 1
            timetrack.append((airplane.end, -1))  # end -= 1

        timetrack.sort()
        res = 0
        globalmax = float('-inf')
        for time, value in timetrack:
            if value == 1:
                res += 1
            else:
                res -= 1
            globalmax = max(globalmax, res)

        return globalmax




