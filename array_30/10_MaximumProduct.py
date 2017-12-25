# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 20:41:08 2017

@author: Administrator
"""

''' Description
Given an integer array, find three numbers whose product is maximum and 
output the maximum product.
Input: [1,2,3，4]
Output: 24
'''
## [-5,-2,0, 2,3,9] 选：2负1正，3正
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)-1
        maxpro2 = nums[n-1]*nums[n-2]
        if nums[0] > 0 or (nums[0] < 0 and nums[1] > 0):
            return nums[n] * maxpro2
        if nums[0]*nums[1] > maxpro2:
            maxpro2 = nums[0]*nums[1]
            
        return nums[n]* maxpro2
                 
        
nums = [-5,9, 3,2,-2,0]
#nums = [3,-9,7,2,1,8]
obj = Solution()
print obj.maximumProduct(nums)