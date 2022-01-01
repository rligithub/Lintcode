class Solution:
    # use stack to keep track index
    # when height increase, append to stack
    # when height decrease --> h = stack.pop(); w = i-1 - stack[-1] #prev pos - last pos in stack
    # please note that i-1 is fixed each time

    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        stack = [-1] # in order to calculate area in index 0 --> w = i-1 - stack[-1]
        heights.append(0) # in order to include last index n --> w = i -1 - stack[-1]
        res = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i -1 - stack[-1]
                res = max(res,h * w)
            stack.append(i)
        return res

heights = [2,0,2,1,1]
a = Solution()
print(a.largestRectangleArea(heights))