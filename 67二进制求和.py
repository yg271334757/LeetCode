# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:22:41 2018

@author: Gang Yang
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(self.bin2dec(a) + self.bin2dec(b)))[2:] 
    def bin2dec(self,x):
        nums = 0
        tem = []
        for j in x:
            tem.append(j)
        tem.reverse()
        for i in range(len(tem)):
            nums += 2 ** i * int(tem[i])
        return nums