# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 13:32:12 2017

@author: Administrator
"""
''' Description
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        res = 0
        for num in nums:
            if num == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res

arr = [1,  0, 1, 1, 1]
obj = Solution()
print obj.findMaxConsecutiveOnes(arr)  