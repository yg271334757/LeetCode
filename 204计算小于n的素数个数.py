# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:21:09 2018

@author: Gang Yang
"""
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        maplist = [1] * n
        maplist[0] = 0
        maplist[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if maplist[i] == 1:
                maplist[i * i : n : i] = [0] * len(maplist[i * i : n : i])
        return sum(maplist)
        