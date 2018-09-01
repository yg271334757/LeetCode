# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:06:32 2018

@author: Gang Yang
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = s.lower()
        res = []
        for i in a:
            if i.isalnum():
                res.append(i)
        b = res.copy()
        res.reverse()
        if b == res:
            return True
        else:
            return False