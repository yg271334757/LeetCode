class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(list(set(nums)))
        if len(s) < 3:
            return max(s)
        return s[-3]