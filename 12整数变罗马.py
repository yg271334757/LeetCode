# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:31:27 2018

@author: Gang Yang
"""
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        values = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        for i in range(len(keys)):
            while num >= keys[i]:
                num -= keys[i]
                res += values[i]
        return res
