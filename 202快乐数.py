# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:14:39 2018

@author: Gang Yang
"""
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tem = []
        res = 0
        for i in str(n):
            res += int(i) ** 2
        tem.append(res)
        while True:
            a = res
            res = 0
            for i in str(a):
                res += int(i) ** 2
            if res == 1:
                return True
            elif res not in tem:
                tem.append(res)
            elif res in tem:
                return False
            