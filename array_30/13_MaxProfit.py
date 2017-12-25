# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:28:30 2017

@author: Administrator
"""
''' Description: 
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
'''
class Solution(object):
    '''
    def maxProfit0(self, prices):  ## 没有解决[3,3,5,0,0,3,1,4]类型
        """
        :type prices: List[int]
        :rtype: int
        """
        # 不能重排序        
        profit = -99999
        idmax = []
        for idx in xrange(1, len(prices)):
            if prices[idx] - prices[0] >= profit:
                profit = prices[idx] - prices[0]
                idmax.append(idx)
        
        profit = 0
        for i in xrange(len(idmax)):            
            for idx in xrange(idmax[i]):
                if prices[idmax[i]] - prices[idx] > profit:
                    profit = prices[idmax[i]] - prices[idx]
                    
        return profit
    '''

    def maxProfit(self, prices):
        maxpro = 0
        minval = 99999
        for idx in xrange(len(prices)):
            minval = min(minval, prices[idx])
            maxpro = max(maxpro, prices[idx]- minval)
        return maxpro
    

#nums = [7, 1, 5, 3, 6, 4]
#nums = [2,1,2,1,0,1,2]
#nums = [1, 2]
nums = [3,3,5,0,0,3,1,4]
obj = Solution()
print obj.maxProfit(nums)

''' 思路
1，要在当前序列中找较小值，并且这个值之后出现较大值
2，遍历一次序列，同时记录 当前最小值 and 当前最大利润
'''