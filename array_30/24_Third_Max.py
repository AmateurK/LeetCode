# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:55:52 2017
#### 给定非空数组，找出第三大的数，Time = O(n) ####
#### 若不存在，则返回最大数 ####
@author: Administrator
"""
import heapq

class Solution(object):
    def thirdMax(self, nums):  ### Time=O(n); Space=O(1)
        m1 = m2 = m3 = min(nums)
        if len(set(nums)) < 3:
            return max(nums)
        for val in nums:
            if val > m1:
                m1, m2, m3 = val, m1, m2  ### 注意应用python的简便操作
            elif val > m2 and val < m1:
                m2, m3 = val, m2
            elif val > m3 and val < m2:
                m3 = val
        return m3
    
    def thirdMax1(self, nums):  ### Time=O(n); Space=O(1)
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
    
    def thirdMax2(self, nums): ### python中的高级数据结构
        m3 = [float('-inf')] * 3
        for n in nums:
            if n > m3[0] and n not in m3:
                heapq.heappushpop(m3, n)
        return m3[0] if m3[0] != float('-inf') else max(m3)
        
        
#nums = [2,2,3,1,6,3,4]
#nums = [1,2,2,5,3,5]
nums = [5,2,4,1,3,6,0]
obj = Solution()
print (obj.thirdMax(nums))