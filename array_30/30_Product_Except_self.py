# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:06:39 2017
##### Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
@author: Administrator
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 1        
        for i in range(len(nums)):
            if nums[i] != 0:
                m = m * nums[i]
            else:
                nums[i] = - nums[i]
        cnt = 0
        for e in nums:
            if e != 0:
                cnt = cnt + 1
            
        if cnt == len(nums):
            nums = [int(m / nums[i]) for i in range(len(nums))]
            return nums
        
        elif cnt == len(nums) - 1:
            for i in range(len(nums)):
                nums[i] = 0 if nums[i] != 0 else m
            return nums
        
        else:
            nums = [0 for e in nums]
            return nums
        
    def productExceptSelf1(self, nums):
        res = [0] * len(nums)
        right, res[0] = 1, 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]
        return res


aa = [1,2,3,4]
#aa = [1,0,2,3,5]
#aa = [1, -1]
#aa = [9,0,-2]
obj = Solution()
print (obj.productExceptSelf(aa))

