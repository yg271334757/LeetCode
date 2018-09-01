# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:26:29 2018

@author: Gang Yang
"""
class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        s = set(nums)
        for i in range(len(s)):
            nums[i] = s(i)
        return len(s)        
            