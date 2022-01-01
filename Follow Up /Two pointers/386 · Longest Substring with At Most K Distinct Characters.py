class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0 or len(s) == 0:
            return 0

        hashset = {}
        left, right = 0, 0
        count, res = 0, 0

        while right < len(s):
            if s[right] not in hashset or hashset[s[right]] == 0:
                count += 1
                hashset.setdefault(s[right], 0)
            hashset[s[right]] += 1
            right += 1

            while count > k:
                hashset[s[left]] -= 1;
                if hashset[s[left]] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left)

        return res