class Solution: #to get subarray's first index and last index, which sum of subarry is closest to 0
    # save all presum and each index in hashmap
    # get minimum of abs(presum1 - presum2), if globalmin is updated, record the presum1 and presum2
    # how to get abs(presum1 - presum2) --> sorted presum first, then compare current presum and previous presum
    # find the index of presum1 and presum2 in hashmap, return
    def subarraySumClosest(self, nums):
        n = len(nums)
        if n == 0:
            return []
        hashmap = {0 : 0}
        presum = 0
        for i in range(n):
            presum += nums[i]
            if presum in hashmap:
                return [hashmap[presum], i]
            hashmap[presum] = i + 1

        # to get two closest presum, which means [presum1 - presum2] is closest to 0
        path = sorted(list(hashmap.keys()))
        globalMin = float('inf')
        for i in range(1,len(path)):
            if abs(path[i] - path[i-1]) < globalMin:
                globalMin = abs(path[i] - path[i-1])
                sum1 = path[i-1]
                sum2 = path[i]

        # to get first index and last index of subarray
        if hashmap[sum1] < hashmap[sum2]:
            return [hashmap[sum1],hashmap[sum2] - 1]
        else:
            return [hashmap[sum2],hashmap[sum1] - 1]



nums = [-3,1,1,-3,5]

a = Solution()
print(a.subarraySumClosest(nums))






