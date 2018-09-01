# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:29:27 2018

@author: Gang Yang
"""
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        maplist = dict(zip(keys, values))
        res = 0
        for i in s:
            res = res * 26 +maplist[i] 
        return res
        
            
            
