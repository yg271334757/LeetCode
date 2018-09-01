# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:31:09 2018

@author: Gang Yang
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if s == ' ':
                return 0
            else:
                return 1
        else:
            a = s.split()
            if a == []:
                return 0
            else:
                return len(a[-1])
            
        