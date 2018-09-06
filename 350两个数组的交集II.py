class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set(nums1)
        b = set(nums2)
        if len(a) >= len(b):
            long = a
            short = b
        else:
            long = b
            short = a
        res = []
        for i in short:
            if i in long:
                res += [i] *  min(nums1.count(i), nums2.count(i))
        return res