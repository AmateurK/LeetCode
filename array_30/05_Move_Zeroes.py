# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 16:15:03 2017

@author: Administrator
"""
''' Description
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums 
should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
#### 思路：把非0数移到最前面，后面添0
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        k = 0
        N = len(nums)
        while i <= N + k-1:
            if nums[i] != 0:
                nums.insert(k, nums[i])
                k += 1
                i += 2
            else:
                i += 1
        del nums[k:]
        nums.extend([0 for i in xrange(N-k)])
        return nums
    
'''##### Better solution: swap the 非0 and 0
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
'''
        
nums = [0,1,0,3,12]
obj = Solution()
print obj.moveZeroes(nums)  
            