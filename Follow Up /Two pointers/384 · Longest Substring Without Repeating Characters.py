class Solution:
    # sliding window - two pointer with same directions
    # use hashset to record what is in the current window
    # use globalmax to record the longest size of sliding window
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        hashset = set()
        maxcount = float('-inf')
        j = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in hashset:
                hashset.add(s[j])
                j += 1
            maxcount = max(maxcount, j - i)  # not j-i+1 because there is j+1 on the previous step
            hashset.remove(s[i])
        return maxcount





