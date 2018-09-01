# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:09:38 2018

@author: Gang Yang
"""
class Solution:
    def threeSum(self, nums):
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
                s = nums[i] + nums[l] + nums[r] 
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:# l去重
                        l += 1
                    while l < r and nums[r] == nums[r+1] :# r 去重
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res

