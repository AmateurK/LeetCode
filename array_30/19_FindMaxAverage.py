# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:54:59 2017

@author: Administrator
"""
'''Description
Given an array consisting of n integers, find the contiguous subarray of 
given length k that has the maximum average value. 
And you need to output the maximum average value.
找特定数目下的最大连续子序列的均值
'''
import numpy as np
import itertools

class Solution(object):
    def findMaxAverage(self, nums, k):
        '''
        nmx = nums[0]        
        for it in xrange(len(nums)-k+1):
            i = it + 1
            c = 1
            cur = nums[it]
            while c < k and i < len(nums):
                cur += nums[i]
                c += 1
                i += 1
            nmx = max(nmx, cur)
        return float(nmx) / k
        '''
# 如果循环计算k个的值，那么会有很多重复计算
# sum + (num[i]-num[i-k])

        ksum = sum(nums[:k])
        res = ksum
        for i in range(k, len(nums)):
            ksum += nums[i] - nums[i-k]
            res = max(res, ksum)
        return float(res) / k
        
    
# 运用python库函数简化代码
    def findMaxAverage1(self, nums, k):
        
        sums = np.cumsum([0] + nums) ## 计算累加和 然后相减
        return float(max(sums[k:] - sums[:-k])) / k
        

k = 4
nums = [1,12,-5,-6,12,3]
#nums = [0,1,1,3,3]
obj = Solution()
print (obj.findMaxAverage1(nums, k))

''' ## itertools 内置模块：用于操作迭代对象
1、itertools.accumulate() 返回累加的和，参数类型不限
2、itertools.chain() 把一组迭代对象串起来，形成更大的迭代器
3、itertools.groupby() 把相邻重复的元素挑出来放一起
'''
## np.cumsum() 对每个元素求累积和，从上到下，从左到右