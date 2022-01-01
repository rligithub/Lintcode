class Solution: # return sum in each sliding window, which window length is k
    # get sum of first k items
    # for each index between k and len(nums), newsum = sum + nums[i] - nums[i-k]

    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        res = []
        sum = 0
        if len(nums) == 0:
            return res

        for i in range(k):
            sum += nums[i]
        res.append(sum)
        for i in range(k,len(nums)):
            sum = sum + nums[i] - nums[i-k]
            res.append(sum)
        return res

array = [1,2,7,8,5]
k = 3
a = Solution()
print(a.winSum(array, k))
