class Solution: # permutation with duplicated values, add visited set to de-duplicated
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        res = []
        self.dfs(nums, res, 0)
        return res

    def dfs(self,nums, res, index):
        if index == len(nums):
            res.append(nums[:])
            return
        visited =set()
        for i in range(index, len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            nums[index], nums[i] = nums[i],nums[index]
            self.dfs(nums, res, index + 1)
            nums[index], nums[i] = nums[i], nums[index]

nums = [1,2,2]
a = Solution()
print(a.permuteUnique(nums))