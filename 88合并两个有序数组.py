# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:23:24 2018

@author: Gang Yang
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m + n < len(nums1):
            return []
        else:
            for i in range(n):
                nums1[m + i] = nums2[i]
        return nums1.sort()
        
