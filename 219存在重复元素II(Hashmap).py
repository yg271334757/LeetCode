# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:18:03 2018

@author: Gang Yang
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        Hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in Hashmap:
                Hashmap[nums[i]] = i
            else:
                if i - Hashmap[nums[i]] <= k:
                    return True
                else:
                    Hashmap[nums[i]] = i
        return False
