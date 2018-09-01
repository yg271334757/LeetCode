# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:28:38 2018

@author: Gang Yang
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x ** 0.5)
        return int(a[:a.index('.')])
