# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:47:05 2018

@author: Gang Yang
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        res = []
        while j > i:
            maxArea = (j - i) * min(height[i], height[j])
            res.append(maxArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max(res)