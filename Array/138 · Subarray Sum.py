class Solution: # to get subarray's first index and last index, which sum of subarry == 0
    # use a hashmap to store {presum: current index }
    # check if presum is exist in hashmap, means that sum from index "hashmap[presum]" to current index i is zero
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        n = len(nums)
        preSum = 0
        hashmap ={0: 0}
        for i in range(n):
            preSum += nums[i]
            if preSum in hashmap:
                return [hashmap[preSum], i]

            hashmap[preSum] = i+1

nums = [-3,1,2,-3,4]
a = Solution()
print(a.subarraySum(nums))