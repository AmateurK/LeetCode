# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 08:47:27 2017

@author: Administrator
DEscription：
Given an array with n integers, your task is to check if it could become 
non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if 
array[i] <= array[i + 1] holds for every i (1 <= i < n).
Input: [4,2,3]
Output: True
"""
class Solution(object):
    def checkPossibility(self, nums): ##大中夹小 or 小中夹大
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in xrange(2, len(nums)):  # Time: O(n^2)
            ## case 1
            if nums[i-2] > nums[i-1] and nums[i-2] > nums[i]:
                cnt = 1                
            if cnt == 1:
                del nums[i-2]
                nn = sorted(nums)
                if nn == nums:
                    return True
                return False
            ## case 2
            if nums[i-2] > nums[i-1] and nums[i-2] < nums[i]:
                cnt = 2
            if cnt == 2:
                del nums[i-1]
                nn = sorted(nums)
                if nn == nums:
                    return True
                return False
            
        return True
    
    def checkPossibility1(self, nums): ##用修正的方式: O(n)
        one, two = nums[:], nums[:]  ###注意nums[:] 与nums的区别
        for i in range(1, len(nums)):  # Time: O(n^2)
            if nums[i-1] > nums[i]:
                one[i] = nums[i-1]  # 2 3 4 1 6
                two[i-1] = nums[i]  # 2 3 4 7 6
                break            
        return one==sorted(one) or two==sorted(two)
                
        

nums = [4,2,3]
obj = Solution()
print (obj.checkPossibility1(nums))
