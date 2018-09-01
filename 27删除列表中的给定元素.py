# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:16:16 2018

@author: Gang Yang
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        else:
            l = 0
            for r in range(len(nums)):
                if nums[r] != val:
                    nums[l] = nums[r]
                    l += 1
            return l
                
                
                