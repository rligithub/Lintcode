class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        # for loop from left to right (add index to stack)
        # if cur_height > prev_height --> height increase, append index to stack
        # while cur_height < prev_height --> height decrease until showing ascending, pop each index from stack, update high and width to get max res
        # high = heights[stack.pop()] , width = cur_index - 1 - stack[-1]
        stack = [-1]
        res = 0
        heights.append(0)

        for i, height in enumerate(heights):
            while i > 0 and height < heights[stack[-1]]:
                high = heights[stack.pop()]
                width = i - 1 - stack[-1]       # i-1 ==> previous index; stack[-1] ==> previous previous index
                res = max(res, high * width)
            stack.append(i)

        return res

heights = [2,1,6,5,2,3]
a = Solution()
print(a.largestRectangleArea(heights))



