# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 21:18:54 2017

@author: Administrator
"""
''' Description: 
unsorted array of integers, find the length of longest continuous increasing subsequence.
Input: [1,3,5,4,7]
Output: 3
'''
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0  ### 考虑空array
        cnt = 1
        maxlen = 1
        for i in xrange(1, len(nums)):
            if nums[i-1] < nums[i]:
                cnt += 1
            else:
                if cnt > maxlen:
                    maxlen = cnt
                cnt = 1
                
        if cnt > maxlen:  ## 考虑单增array
            maxlen = cnt
                
        return maxlen
            
        
        
nums = [1,3,5,4,7,0,2]
obj = Solution()
print obj.findLengthOfLCIS(nums)