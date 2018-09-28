class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        sumNums = sum(nums)
        repNum = sumNums - sum(set(nums))
        missNum = len(nums) * (1 + len(nums)) // 2 - sum(set(nums))
        return [repNum, missNum]