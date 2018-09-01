# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:41:39 2018

@author: Gang Yang
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n_2 = bin(n)[2:]
        nums_0 = '0' * (32 - len(n_2))
        tem = nums_0 + n_2
        res = 0
        for i in range(len(tem)):
            res += int(tem[i]) * 2 ** i
        return res
