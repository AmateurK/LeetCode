# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:06:15 2017

@author: Administrator
"""
''' Description
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ #折半查找效率高
        low = 0
        high = len(nums) - 1
        mid = (low + high) / 2              
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    high = mid - 1
                else: 
                    low = mid + 1
        return low
        
    def searchInsert1(self, nums, target): ###### Perfect !!
        return len([x for x in nums if x < target])


nums = [1,3,6,12]
obj = Solution()
print obj.searchInsert1(nums, 6)