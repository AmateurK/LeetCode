# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:28:28 2017

@author: Administrator
"""
''' Description
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray1(self, nums): ### O(n^3) 穷举法
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                cursum = 0
                for k in xrange(i, j):  #大量重复计算
                    cursum += nums[k]
                if cursum > maxsum:
                    maxsum = cursum                    
        return maxsum
    
    def maxSubArray2(self, nums): ### O(n^2) 穷举法
        maxsum = nums[0]
        for i in xrange(len(nums)):
            cursum = 0
            for j in xrange(i, len(nums)):
                cursum += nums[j]
                if cursum > maxsum:
                    maxsum = cursum
        return maxsum
        
    
    def maxSubArray3(self, nums): ### O(n) 常用的动态规划法(arr全是负数则出错)
        maxsum = cursum = nums[0]
        for i in xrange(len(nums)):
            cursum += nums[i]
            if cursum > maxsum:
                maxsum = cursum
            else:
                if cursum < 0:
                    cursum = nums[i]
        return maxsum
        
    
    def maxSubArray4(self, nums): ### O(n)  Perfect!!!
        maxsum = cursum = nums[0]
        for i in xrange(1, len(nums)):
            cursum = max(nums[i], cursum+nums[i])
            maxsum = max(maxsum, cursum)            
        return maxsum
    
    def maxSubArray5(self, nums): ### O(n)  Right!!!
        maxsum = cursum = nums[0]
        for i in xrange(1, len(nums)):
            if cursum < 0:
                cursum = nums[i]
            else:
                cursum += nums[i]
            if cursum > maxsum:
                maxsum = cursum            
        return maxsum
    

nums = [-3,-2,-1]
#nums = [-2,2,-4,6,0,-2,9,-3]
obj = Solution()
print obj.maxSubArray4(nums)