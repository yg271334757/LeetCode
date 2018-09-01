# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:40:28 2018

@author: Gang Yang
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == sorted(prices, reverse = True):
            return 0
        elif prices == sorted(prices):
            return prices[-1] - prices[0]
        else:
            profit = 0
            price = prices[0]
            for i in prices:
                if i - price > 0:
                    profit += i - price
                    price = i
                elif i < price:
                    price = i
            return profit
            
