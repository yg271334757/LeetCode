# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:55:09 2018

@author: Gang Yang
"""
# [7,1,5,3,6,4]
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == sorted(prices, reverse = True):
            return 0
        else:
            min_price = prices[0]
            max_profit = 0
            for i in prices:
                if i < min_price:
                    min_price = i
                elif i - min_price > max_profit:
                    max_profit = i - min_price
            return max_profit
