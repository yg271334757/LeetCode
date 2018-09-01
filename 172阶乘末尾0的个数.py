# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:31:14 2018

@author: Gang Yang
"""
class Solution:
    def trailingZeroes(self,n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while n // 5**i > 0:
            count += n//5**i
            i += 1
        return count
