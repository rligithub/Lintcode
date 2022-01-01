class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # to make sure there is no repeat value in path, move to next index when we do dfs (not repeatly consider current index value)
        path, res = [],[]
        num = sorted(num)
        if len(num) == 0:
            return

        self.dfs(num, target, 0, path, res)
        return res

    def dfs(self, num, target, index, path, res):
        if target == 0 and path not in res:
            return res.append(path)
        for i in range(index,len(num)):
            if target < num[i]:
                break

            self.dfs(num, target - num[i], i+1, path + [num[i]], res)


num = [7,1,2,5,1,6,10]
target = 8
a = Solution()
print(a.combinationSum2(num, target))