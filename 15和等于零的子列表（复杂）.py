# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:49:50 2018

@author: Gang Yang
"""
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            a = i + 1
            while a < len(nums) - 1:
                b = a + 1
                while b < len(nums) :
                    if nums[i] + nums[a] + nums[b] == 0:
                        res.append([nums[i], nums[a], nums[b]])
                    b += 1
                a += 1
        return del_dup(res)
def del_dup(x):
    res = []
    for i in x:
        if i not in res:
            res.append(i)
    return res
                
                    
