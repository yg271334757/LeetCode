# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:59:53 2018

@author: Gang Yang
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
