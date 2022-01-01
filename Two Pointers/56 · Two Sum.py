class Solution: # return index of two numbers in array, which sum of these two numbers equal to target
    # use a hashmap to store the num and its index, {numbers:index}
    # for loop to see if [target - num1] in hashmap, if yes, return index of num1 and index of [target - num2]
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if len(numbers) == 0:
            return []
        # hashtable can be replaced by using enumerate( ) function --> [index, num]
        hashtable = {}
        for i in range(len(numbers)):
            hashtable[numbers[i]] = i

        print(hashtable)
        for i in range(len(numbers)):
            if target - numbers[i] in hashtable.keys():
                return [i,hashtable[target - numbers[i]]]

class Solution2: # same solution to solution1
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, nums, target):
        if not nums:
            return []
        table = {}
        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num],i]
            table[num] = i

numbers = [15,2,7,11]
target = 9
a = Solution()
print(a.twoSum(numbers, target))