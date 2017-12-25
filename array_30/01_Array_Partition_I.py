# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 09:34:10 2017

@author: Administrator
"""


class Solution(object):
    def arrayPairSum(self, arr):
        arr.sort()
        sumarr = 0
        for i in range(0, len(arr)-1, 2):
            sumarr += arr[i]
        return sumarr
    
arr = [2,4,3,1]
obj = Solution()
print obj.arrayPairSum(arr)
