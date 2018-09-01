# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:22:17 2018

@author: Gang Yang
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        elif needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
