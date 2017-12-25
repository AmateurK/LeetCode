# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 10:04:11 2017

@author: Administrator
"""
#### Time O(n), space O(1)
## 可以用arr[n]作为标记数组，但是space不允许，
## 所以每个位置的数字出现以后，需要在原来数字上做标记，可以用加负号的方式
## 别的方式都不行 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1 #注意先变成正数再判断
            nums[index] = - abs(nums[index])  ######方法很巧妙
        return [i+1 for i in xrange(len(nums)) if nums[i] > 0]
                        
    
nums = [2,2,3,5,1,1]
obj = Solution()
print obj.findDisappearedNumbers(nums)  


'''##### 超时
class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        ans = sorted(set(nums))
        res = []        
        if ans[0] != 1:
            res.append(1)
        if ans[len(ans)-1] != len(nums):
            res.append(len(nums))
        k = 1
        while k < len(nums):
            if nums[k] - nums[k-1] > 1:
                rec = nums[k-1] + 1
                while rec != nums[k]:
                    res.append(rec)
                    rec += 1
            k += 1
        res.sort()
        return res
'''
