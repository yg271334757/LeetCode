class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) >= len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
        res = []
        for i in b:
            if i in a and i not in res:
                res.append(i)
        return res  