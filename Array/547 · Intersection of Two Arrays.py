class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for num in set2:
            if num in set1:
                res.append(num)
        return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

a = Solution()
print(a.intersection(nums1, nums2))