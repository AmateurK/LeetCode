# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 17:43:20 2017

@author: Administrator
"""
''' Description
Say you have an array for which the ith element is the price of a given 
stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                sum += prices[i] - prices[i-1]                
        return sum
        
        
nums = [2,1,3,5,2,6]
obj = Solution()
print obj.maxProfit(nums)  

'''
def maxProfit(self, prices):
    return sum(max(prices[i]-prices[i-1], 0) for i in range(1, len(prices)))
'''