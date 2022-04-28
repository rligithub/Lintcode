class Solution: #recursion --> add current value vs not add current value
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        res, path = [], []
        nums = sorted(nums)
        self.dfs(nums, res, path, 0)
        return res

    def dfs(self, nums, res, path, index):
        if index == len(nums):
            return res.append(path)
        self.dfs(nums, res, path, index +1)
        self.dfs(nums,res,path + [nums[index]], index +1)

class Solution2: #recursion --> add current value vs not add current value
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        res, path = [], []
        nums = sorted(nums)
        self.dfs(nums, res, path, 0)
        return res

    def dfs(self, nums, res, path, index):

        for i in range(index,len(nums)):
            self.dfs(nums, res, path + [nums[i]], i +1)
        return res.append(path)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        res = []
        path = []
        nums = sorted(nums)
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, pos, res, path):
        if pos == len(nums):
            res.append(path)
            return
        self.dfs(nums, pos + 1, res, path + [nums[pos]])
        self.dfs(nums, pos + 1, res, path)


nums = [1,2]

a = Solution2()
print(a.subsets(nums))
