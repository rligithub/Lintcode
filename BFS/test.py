import collections


class Solution:
    def minimizeTheDifference(self, mat, target):

        queue = collections.deque()
        n = len(mat)
        queue.append([0] * n)
        res = float('inf')
        mat = [sorted(nums) for nums in mat]
        while queue:
            size = len(list(queue))
            for i in range(size):
                node = queue.popleft()
                summ = 0
                for i, nums in zip(node, mat):
                    summ += nums[i]
                if summ == target:
                    return 0
                res = min(res, abs(target) - summ)

                for i in range(n):
                    newNode = list(node)[:i] + [list(node)[i]+1] + list(node)[i+1:]
                    queue.append(newNode)

        return res


mat = [[1],[2],[3]]
target = 100

a = Solution()
print(a.minimizeTheDifference(mat, target))

