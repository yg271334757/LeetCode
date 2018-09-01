# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:36:56 2018

@author: Gang Yang
"""
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        nums.sort()
        return nums.index(target)
