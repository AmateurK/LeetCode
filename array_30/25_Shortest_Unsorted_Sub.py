# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:55:52 2017
#### 找连续子数组，按升序对其排序后，整个数组也将升序有序，
#### 你需要找到这样最短的子数组并输出它的长度。 ####
@author: Administrator
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aa = sorted(nums)
        if aa == nums:
            return 0         
        ind = []
        for i in range(len(nums)):
            if nums[i] != aa[i]:
                ind.append(i)                
        return ind[-1] - ind[0] + 1 
        
    def findUnsortedSubarray1(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same)  \
                else len(nums) - is_same.index(False) - is_same[::-1].index(False)
        
        

nums = [2, 6, 4, 8, 10, 9, 15]
obj = Solution()
print (obj.findUnsortedSubarray(nums))