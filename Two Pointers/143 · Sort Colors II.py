import collections


class Solution: # count how many same color for each color, then replace colors[i] for each colors
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        n = len(colors)
        nums = [0] * (k+1)

        for num in colors:
            nums[num] += 1
        i = 0
        for color, count in enumerate(nums):
            while count > 0:
                colors[i] = color
                i += 1
                count -= 1
        return colors


colors = [2,1,1,2,2]
k = 2
a = Solution()
print(a.sortColors2(colors,k))