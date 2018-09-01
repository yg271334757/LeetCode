# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:29:58 2018

@author: Gang Yang
"""
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            elif t[i] in dic.values():
                return False
            else:
                dic[s[i]] = t[i]
        return True