class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        if not nums:
            return 0
        pos = 0
        maxL = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                maxL = max(i - pos + 1, maxL)
            else:
                pos = i  
        return maxL