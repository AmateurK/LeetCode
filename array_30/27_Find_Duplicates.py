# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:04:20 2017
#########  Description  ###########
#### 给定 1 ≤ a[i] ≤ n (n = size of array)，找出现两次的数（只有出现一次或两次的数字）
#### space：O(1); Time：O(n)  #####

@author: Administrator
"""
''' ### 总结  ###
  1，Space和Time有限的情况下，用符号在原地标记。
  2，或者原地交换
'''
class Solution(object):
    def findDuplicates(self, nums):  ## 交换数组中元素
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
#                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                ### Error原因：这样[]里面的数会变，所以出错
            else:
                i += 1
        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res


    def findDuplicates1(self, nums):  ## 用符号进行标记
        res = []
        for e in nums:
            if nums[abs(e)-1] > 0:
                nums[abs(e)-1] *= -1
            else:
                res.append(abs(e))
        return res

        
nums = [4,3,2,7,8,2,3,1]  # out：[2,3]
obj = Solution()
print (obj.findDuplicates1(nums))