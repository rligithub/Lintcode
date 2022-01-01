class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        res = ""
        left = 0
        minLen = float('inf')
        total = 0
        count = collections.Counter(target)

        for i, char in enumerate(source):
            count[char] -= 1
            if count[char] >= 0:
                total += 1
            while total == len(target):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = source[left: i + 1]
                count[source[left]] += 1
                if count[source[left]] > 0:
                    total -= 1
                left += 1
        return res