# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:45:36 2018

@author: Gang Yang
"""
class Solution:
    def threeSumClosest( nums,target):
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]: # i去重
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val - target == 0:
                    return val
                elif val - target < 0:
                    res.append(val)
                    l += 1
                else:
                    res.append(val)
                    r -= 1
        final = list(map(lambda x: abs(x - target), res))   
        return res[final.index(min(final))]
                


            
            
