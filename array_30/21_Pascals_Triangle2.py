# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 15:34:52 2017
@author: Administrator

### Descirption
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
use only O(k) extra space
"""
import numpy as np

class Solution(object):
    def getRow(self, rowIndex): ## 运用生成pascal矩阵的方式，space：O((n+n^2)/2)
        if rowIndex < 1:
            return [[1]]
        
        res = [[1, 1]]
        for i in xrange(1, rowIndex):
            res += [map(lambda x, y: x+y, [0] + res[-1], res[-1] + [0])]
            
        cur = res[-1]
        return cur
    
    def getRow1(self, rowIndex): ## space: O(k)
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1): ## 这里注意倒序
                res[j] += res[j-1]
        return res
        
        
obj = Solution()
print (obj.getRow1(4))