# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 13:36:02 2017

@author: Administrator
"""
''' Description (有序)
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
#### 本质：两端查找，效率最高（快排思想）
class Solution1(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [i for i in numbers]
        nums.sort()
        low = 0
        high = len(nums)-1
        for k in xrange(len(nums)):
            if nums[low] + nums[high] > target:
                high -= 1
            if nums[low] + nums[high] < target:
                low += 1
        return [low+1, high+1]
    
    
''' Description（无序）###用dict结构标记元素排序后的位置
Input: numbers=[3, 2, 4], target=6
Output: [1, 2]
'''    
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mm = {}
        for i in xrange(len(nums)):
            mm[i] = nums[i]

        mm = sorted(mm.items(), key=lambda d:d[1])
        
        for j in xrange(len(mm)):
            nums[j] = list(mm[j])
        
        low = 0
        high = len(nums)-1
        for k in xrange(len(nums)):
            if nums[low][1] + nums[high][1] > target:
                high -= 1
            if nums[low][1] + nums[high][1] < target:
                low += 1
                
        if nums[low][0] > nums[high][0]:
            nums[low][0], nums[high][0] = nums[high][0], nums[low][0]
            
        return [nums[low][0], nums[high][0]]
    
    
    def twoSum2(self, nums, target): ###借助 enumerate函数,num 作为key存储
        dnum = {}
        for idx, item in enumerate(nums):
            if dnum.has_key(item):
                return [dnum[item], idx]
            else:
                dnum[target - item] = idx
                    
    ##### Perfect #####        
    def twoSum3(self, nums, target): ###借助 enumerate函数，num 作为key存储
        dnum = {}
        for idx, num in enumerate(nums):
            if target-num in dnum:
                return [dnum[target - num], idx]
            dnum[num] = idx
        

nums = {2,3,5}
obj = Solution1()
print obj.twoSum(nums, 5)

nums = [3,2,4, 9, 0, 1]
obj = Solution()
print obj.twoSum3(nums, 10)  