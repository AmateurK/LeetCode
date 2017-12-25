# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 18:33:30 2017

@author: Administrator
"""
''' Description
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element 
always exist in the array.
[2,2,7,2,4,2,4,2,2,2,9]
2
'''
#### 找出超过n/2次数的元素
class Solution(object):
    def majorityElement(self, nums): #排序后最中间的数
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
    
    def majorityElement2(self, nums): #标记得到数目最多的数字
        idx = 1
        maj = nums[0]
        cnt = 1
        while idx < len(nums):
            if cnt == 0:
                maj = nums[idx]
                cnt += 1
            else:
                if maj == nums[idx]:
                    cnt += 1
                else:
                    cnt -= 1
            idx += 1
        return maj

    
#nums = [2,2,7,2,4,2,4,2,2,2,9]
#nums = [3,2,3]
#nums = [-1,1,1,1,2,1]
nums = [6,5,5]
obj = Solution()
print obj.majorityElement(nums)