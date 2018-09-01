# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 09:57:06 2018

@author: Gang Yang
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strs = []
        for i in digits:
            strs.append(str(i))
        nums = str(int(''.join(strs)) + 1)
        res = []
        for j in nums:
            res.append(int(j))
        return res
        
        
        