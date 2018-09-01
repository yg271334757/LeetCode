# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:58:45 2018

@author: Gang Yang
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            res = [0] * len(nums)
            res[0] = nums[0]
            res[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                res[i] = max(res[i - 1], res[i - 2] + nums[i])
            return res[-1]
