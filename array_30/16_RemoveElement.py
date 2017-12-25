# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:36:22 2017

@author: Administrator
"""
''' Description
remove all instances of that value in place and return the new length.
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
NOTE: constant memory.
'''
class Solution(object):    
    def removeElement(self, nums, val):  ####找出长度 & 移动元素到数组的前半部分
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1                
        return idx
            
    
nums = [3,2,1,3,0,4,3]
#nums = [-2,2,-4,6,0,-2,9,-3]
obj = Solution()
print obj.removeElement(nums, 3)