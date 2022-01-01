class Solution: # return the sum of three numbers in array, which sum is closest to target
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if len(numbers) == 0:
            return 0
        numbers.sort()
        globalmin = float('inf')

        for i in range(0,len(numbers)):
            left, right = i+1, len(numbers) - 1
            while left < right:
                total = numbers[i] + numbers[left] + numbers[right]
                if abs(target - total) < globalmin:
                    globalmin = min(globalmin, abs(target - total))
                    res = total
                if total == target:
                    res = total
                    break
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return res

numbers = [2,7,11,15]
target = 3
a = Solution()
print(a.threeSumClosest(numbers, target))