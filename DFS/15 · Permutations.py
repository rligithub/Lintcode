class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        res = []
        self.dfs(nums, res, 0)
        return res

    def dfs(self, nums, res, index):
        if index == len(nums):
            res.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[index],nums[i] = nums[i],nums[index]
            self.dfs(nums, res, index + 1)  # why not i+1 ????
            nums[index], nums[i] = nums[i], nums[index]

list = [1,2,3]
a = Solution()
print(a.permute(list))

