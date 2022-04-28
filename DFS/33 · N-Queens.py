class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # place Q in row by row --> ensure it's not in the same row
        # before place Q, need to check if it's validQ -- > make sure it's not in the same column and diagonal line
        # use recursion -> row + 1 , path = "." * i + Q + "." * (n-i)
        res = []
        nums = [-1] * n # n为row，里面存的是col
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            nums[index] = i     # set Q's index in each row (try from 0 - n)
            if self.valid(nums, index):
                board = "." * len(nums)
                self.dfs(nums, index + 1, path + [board[:i] + 'Q' + board[i + 1:]], res)

    def valid(self, nums, index):
        for i in range(index):
            # 检查 col是否相同 和 斜线是否相同 (COL1-COL2)/(ROW1-ROW2）
            if nums[i] == nums[index] or abs(nums[i] - nums[index]) == abs(index - i):
                return False
        return True

n = 1
a = Solution()
print(a.solveNQueens(n))