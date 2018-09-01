# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:56:33 2018

@author: Gang Yang
"""
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) != len(nums) else False
