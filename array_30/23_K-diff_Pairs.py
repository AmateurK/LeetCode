# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:20:00 2017
## 给定一个整数和一个整数k的数组，你需要找到数组中唯一的k-diff对的个数。 
## 这里k-diff对被定义为一个整数对（i，j），其中i和j都是数组中的数字，它们的绝对差值是k。
@author: Administrator
"""
import numpy as np
import collections

class Solution(object):
    def findPairs(self, nums, k):  ## 思路一致，但没实现好
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """       
        if k < 0:
            return 0
        elif k == 0:  ### error
            ## 建字典，统计每个数字出现的次数，>2，则cnt+1
                        
            return 
        else:
            return len(set(nums) & set(n+k for n in nums))
#            nums = list(set(nums))
#            km = [k] * len(nums)
#            add_k = list(np.add(nums, km))
#            print([e for e in add_k if e in nums])
#            return len([e for e in add_k if e in nums])
    
    def findPairs1(self, nums, k):  ## Counter()函数是关键
        if k > 0:
            return len(set(nums) & set(n+k for n in nums))
        elif k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0
        ### 一行实现  ###
        return len(set(nums) & {n+k for n in nums}) if k>0 \
                else sum(v>1 for v in collections.Counter(nums).values()) \
                if k==0 else 0
        ###############

    def findPairs2(self, nums, k):
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res
        ### 一行实现 ###        
        c = collections.Counter(nums)
        return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
        ###############

k = 0
nums = [3, 1, 4, 1, 5, 6,7,10]
#nums = [1,1,1,1]
obj = Solution()
print (obj.findPairs1(nums, k))

    