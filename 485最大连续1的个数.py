class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1 = 0
        dp2 = 0
        for i in nums:
            if i == 1:
                dp1 += 1
            else:
                if dp1 > dp2:
                    dp2 = dp1
                    dp1 = 0
                else:
                    dp1 = 0
        return max(dp2, dp1)