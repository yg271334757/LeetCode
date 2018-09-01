# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:46:51 2018

@author: Gang Yang
"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n ==2:
            return 2
        else:
            a = [0 for i in range(n)]
            a[0] = 1
            a[1] = 2
            j = 2
            while j < n:
                a[j] = a[j - 1] + a[j - 2]
                j += 1
            return a[-1]