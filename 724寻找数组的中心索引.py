class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumL = 0
        sumN = sum(nums)
        i = 0
        while i < len(nums):
            if 2 * sumL == sumN - nums[i]:
                return i
            sumL += nums[i]
            i += 1
        return -1