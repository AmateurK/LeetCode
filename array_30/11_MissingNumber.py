# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 21:00:07 2017

@author: Administrator
"""
''' Description
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.
For example, Given nums = [0, 1, 3] return 2.
Note: linear runtime complexity. constant extra space complexity
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[len(nums)-1] != len(nums):
            return len(nums)
        for idx in xrange(len(nums)):
            if idx != nums[idx]:
                return idx



#nums = [4,6,3,1,5,0]  ##case1: basic
nums = [0,1,2]  ## case2: special
obj = Solution()
print obj.missingNumber(nums)     