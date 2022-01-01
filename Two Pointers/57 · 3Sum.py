class Solution: # return three numbers, whose sum == 0
        # use for loop and while loop, fast and slow pointers (two pointers with opposite directions)
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        n = len(numbers)
        if n == 0:
            return []
        numbers.sort()
        res = []

        for i in range(n):

            left, right = i + 1, n - 1
            while left < right:
                total = numbers[i] + numbers[left] + numbers[right]
                if total == 0:
                    sol = [numbers[i],numbers[left], numbers[right]]
                    if sol not in res:      # de-duplicated in solution
                        res.append(sol)
                    left += 1
                    right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res

class Solution2:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        n = len(numbers)
        if n == 0:
            return []
        numbers.sort()
        res = []

        for i in range(n):
            # de-duplicted for i pointer
            if i == 0 or i > 0 and numbers[i - 1] != numbers[i]:
                left, right = i + 1, n - 1
                while left < right:
                    total = numbers[i] + numbers[left] + numbers[right]
                    if total == 0:
                        sol = [numbers[i],numbers[left], numbers[right]]
                        res.append(sol)
                        left += 1
                        right -= 1
                        # de-duplicated for left pointer
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        # de-duplicated for right pointer
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1

                    elif total > 0:
                        right -= 1
                    else:
                        left += 1
        return res

numbers = [1,0,-1,-1,-1,-1,0,1,1,1]
a = Solution2()
print(a.threeSum(numbers))
