class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == [0]:
            return 1
        return sum(range(len(nums) + 1)) - sum(nums)