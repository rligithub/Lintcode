class Solution:  # Bruce force
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        if not nums:
            return
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


class Solution2:  # Two pointer
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        if not nums:
            return
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                fast = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow


class Solution3:  # 这道题是有序的 --> binary search
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """

    def findDuplicate(self, nums):
        if not nums:
            return
        left, right = 0, len(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            # count how many nums are less than mid
            if self.number(nums, mid) < mid:  # if count < mid --> search right side
                left = mid
            else:
                right = mid
        return left

    def number(self, array, mid):
        count = 0
        for num in array:
            if num < mid:
                count += 1
        return count













