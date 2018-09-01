# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:23:40 2018

@author: Gang Yang
"""
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
    # def isPowerOfTwo( n):
    #    """
    #    :type n: int
    #    :rtype: bool
    #    """
    #    if n <=0:
    #        return False
    #    while n>1:
    #        if n&1 ==1:
    #            return False
    #        n>>=1
    #    return True
        if n < 0:
            return False
        a = bin(n)
        if a.count('1') == 1:
            return True
        else:
            return False

