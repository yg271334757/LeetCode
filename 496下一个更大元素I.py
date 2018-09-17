class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            for j in range(nums2.index(i), len(nums2)):
                if i < nums2[j]:
                    res.append(nums2[j])
                    break
            if len(res) == nums1.index(i) + 1:
                continue
            else:
                res.append(-1)
        return res