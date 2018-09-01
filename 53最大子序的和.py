# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:11:34 2018

@author: Gang Yang
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
        
                
                    
            
        
        
                
            
                