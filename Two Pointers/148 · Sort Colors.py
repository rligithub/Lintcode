class Solution1: # use twice two pointer from opposite directions
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        index, nums = self.twoPointer(nums, 0, len(nums) - 1, 0)
        self.twoPointer(nums, index, len(nums) - 1, 1)
        return nums

    def twoPointer(self, nums, left, right, color):
        if len(nums) == 0:
            return None, []
        while left <= right:
            if nums[left] == color:
                left += 1
                continue
            if nums[right] != color:
                right -= 1
                continue
            if nums[left] != color and nums[right] == color:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left, nums

class Solution2: # use twice two pointer from opposite directions
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        n =len(nums)
        if n ==0:
            return []

        r = 0 #0
        w = 0 #1
        b = n -1 #2

        while w < n and w <= b:
            if nums[w] == 0:
                nums[w],nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else: #nums[w] == 2
                nums[w],nums[b] = nums[b], nums[w]
                b -= 1
        return nums




nums = [1, 0, 1, 2]
a = Solution2()
print(a.sortColors(nums))