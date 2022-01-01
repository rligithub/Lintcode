import collections


class Solution1: # two for loop and 2SUM
    # two pointers --> i < j < left
    # two pointers --> right
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        n = len(numbers)
        if n < 4:
            return []
        numbers.sort()
        res = []
        for i in range(n):
            for j in range(i+1, n):
                left, right = j+1, n-1
                while left < right:
                    total = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if total == target:
                        sol = [numbers[i], numbers[j], numbers[left], numbers[right]]
                        if sol not in res:
                            res.append(sol)
                            right -= 1
                            left += 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return res

class Solution2: # two hashmap
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        dic = collections.defaultdict(set)
        n = len(nums)
        nums.sort()

        if n < 4:
            return []
        res = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                sum = nums[i] + nums[j]
                for x, y in dic[target - sum]:
                    res.add(tuple([x, y] + [nums[j], nums[i]]))

            for j in range(i):
                dic[nums[i] + nums[j]].add((nums[j], nums[i]))

        return list(res)

numbers = [1,2,3,4,5,6,7]
target = 18
a = Solution2()
print(a.fourSum(numbers,target))