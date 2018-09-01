# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:31:57 2018

@author: Gang Yang
"""
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tem = k % len(nums)
        if tem == 0:
            nums = nums
        else:
            nums = self.rotate_x(nums, tem)
        
    def rotate_x(self, x, n):
        b = x.copy()
        b.reverse()
        i = 0
        while i <= n:
            x[i] = b[n - i - 1]
            i += 1
        j = 0
        while j < len(x) - n:
            x[n + j] = b[len(x) - j - 1]
            j += 1
        return x