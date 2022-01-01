import collections


class Solution:# use hashmap to store sorted string , then check if the string is in the hashmap more than twice
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        if len(strs) == 0:
            return []
        hashmap = collections.defaultdict(int)
        res = []
        for string in strs:
            string = ''.join(sorted(string))
            hashmap[string] += 1

        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in hashmap and hashmap[sortedString] >1:
                res.append(string)
        return res

strs = ["lint", "intl", "inlt", "code"]
a = Solution()
print(a.anagrams(strs))


