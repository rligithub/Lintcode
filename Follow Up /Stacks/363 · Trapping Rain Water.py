class Solution:
    # two pointers
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # two pointers with opposite directions
        # if heights[left] < heights[right] --> maintain maxleft height, calculate
        # elif heights[left] >= heights[right] --> maintain maxright heights, calculate
        # stop point --> left == right 左右指针相遇

        if not heights:
            return 0
        left, right = 0, len(heights) - 1
        maxleft, maxright = float('-inf'), float('-inf')
        res = 0
        while left < right:
            if heights[left] < heights[right]:
                maxleft = max(maxleft, heights[left])
                res += maxleft - heights[left]
                left += 1
            else:
                maxright = max(maxright, heights[right])
                res += maxright - heights[right]
                right -= 1

        return res


class Solution2:  # stack
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        # use stack
        # if stack[-1] > heights[i] --> stack.append(i)
        # elif stack[-1] <= height[i] --> means heights[stack.pop()] would be lowerest, calculate water on each height
        # h = min(height[stack[-1]], heights[i]) -  heights[stack.pop()]
        # w = i - stack[-1] - 1
        # water = h * w

        if not heights:
            return 0
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                base = heights[stack.pop()]
                if not stack:
                    continue
                h = min(heights[stack[-1]], heights[i]) - base
                w = i - stack[-1] - 1
                res += w * h
            stack.append(i)
        return res



