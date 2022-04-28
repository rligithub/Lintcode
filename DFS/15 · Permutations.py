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

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashset = []
        self.dfs(nums, res, hashset)
        return res

    def dfs(self, nums, res, hashset):
        if len(hashset) == len(nums):
            res.append(hashset)
            return
        for num in nums:
            if num not in hashset:
                self.dfs(nums, res, hashset + [num])
list = [1,2,3]
a = Solution()
print(a.permute(list))

