import collections
class Solution: #deque -->--> 检查没超界--> 保持一个降序 --> 什么时候pop --> 什么时候append res
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # for loop一遍，边做边检查
        # 维持一个降序在deque里，如果进来的数比deque最右边的数要大，就pop
        # 每次进来一个数
        # 检查deque最左边的数（即最大值）是否还在window范围里 i - deque[0] > k-1
        # 什么时候append res --> 当 i>= K-1时（即window范围满足）

        if not nums or k == 0:
            return []
        res = []
        deque = collections.deque()

        for i in range(len(nums)):
            if deque and i - deque[0] > k-1:
                deque.popleft()
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)

            if i >= k-1:
                res.append(nums[deque[0]])

        return res
nums = [1,3,-1,-3,5,3,6,7]
k = 3
a = Solution()
print(a.maxSlidingWindow(nums, k))
