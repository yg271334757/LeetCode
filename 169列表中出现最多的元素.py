# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 19:49:26 2018

@author: Gang Yang
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        b = []
        for i in a:
            a.append(nums.count(i))
        dic = dict(zip(b, a))
        return dic[max(dic)]