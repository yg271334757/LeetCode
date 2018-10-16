class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        a = sorted(set(nums))
        if a[-1] >= a[-2] * 2:
            return nums.index(a[-1])
        else:
            return -1