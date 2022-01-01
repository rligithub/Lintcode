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




candidates = [2, 3, 6, 7]
target = 7
a = Solution()
print(a.combinationSum(candidates,target))
