import collections


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, nums, target):
        nums = sorted(list(set(nums)))
        res = []
        path =[]

        if len(nums) ==0:
            return res
        self.dfs(nums, target, 0, path, res)
        return res

    def dfs(self, nums, target,index, path,res):
        if target == 0:
            return res.append(path)

        for i in range(index,len(nums)):
            if target < nums[i]:
                break
            self.dfs(nums,target - nums[i], i, path + [nums[i]], res)

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, nums, target):
        res = []
        path = []
        nums =sorted(set(nums))
        self.dfs(nums, 0, res, path, 0, target)
        return res

    def dfs(self, nums, pos, res, path, summ, target):
        if summ == target:
            res.append(path)
            return

        for i in range(pos,len(nums)):
            if summ + nums[i] > target:
                break
            self.dfs(nums, i, res, path + [nums[i]], summ + nums[i], target)


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, nums, target):
        res = []
        path = []
        nums =sorted(set(nums))
        self.dfs(nums, 0, res, path, 0, target)
        return res

    def dfs(self, nums, pos, res, path, summ, target):

        if summ >target:
            return
        if summ == target:
            res.append(path)
            return
        self.dfs(nums,pos, res, path+[nums[pos]], summ + nums[pos], target)

        if pos >= len(nums) - 1:
            return

        self.dfs(nums, pos + 1, res,path, summ, target)

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, nums, target):
        res = []
        path = []
        nums =sorted(set(nums))
        self.dfs(nums, 0, res, path, 0, target)
        return res

    def dfs(self, nums, pos, res, path, summ, target):

        if summ >target:
            return
        if summ == target:
            res.append(path)
            return
        if pos == len(nums):
            return
        self.dfs(nums,pos, res, path+[nums[pos]], summ + nums[pos], target)

        self.dfs(nums, pos + 1, res,path, summ, target)


candidates = [2, 3, 6, 7]
target = 7
a = Solution()
print(a.combinationSum(candidates,target))
