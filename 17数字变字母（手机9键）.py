# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:30:00 2018

@author: Gang Yang
"""
import itertools
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        maps = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv','9':'wxyz'}
        tem = []
        for i in digits:
            tem.append(list(maps[i]))
        result = []
        for t in list(itertools.product(*tem)):
            result.append(''.join(t))
        return result
        
            
        