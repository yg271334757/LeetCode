# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:43:05 2018

@author: Gang Yang
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
