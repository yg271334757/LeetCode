# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:12:34 2018

@author: Gang Yang
"""
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        maplist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        res = ''
        while n > 0:
            res += maplist[(n - 1) % 26]
            n = (n - 1) // 26
        return res[::-1]
            