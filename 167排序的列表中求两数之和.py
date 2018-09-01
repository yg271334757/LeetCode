# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:37:20 2018

@author: Gang Yang
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1 , r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
