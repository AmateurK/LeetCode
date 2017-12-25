# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:43:27 2017

@author: Administrator
"""
''' Description
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,  Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in xrange(numRows):
            res.append([1] * (i+1))
            for j in xrange(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]                
        return res
    
    def generate1(self, numRows):
        num = [[1], [1, 1]]
        if numRows == 1:
            return num[0]
        elif numRows == 2:
            return num
        elif numRows == 0:
            return []
        
        row = []
        for i in range(1, numRows):
            for j in range(i):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []
        return num
    
    def generate2(self, numRows): ####### 思路清奇 Perfect！！！
        res = [[1]]
        for i in xrange(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])] ##res[-1] = res[i-1]
        return res
        
    def generate3(self, numRows): ### 两种思路的结合
        res = []
        for i in xrange(numRows):
            res.append([1]*(i+1))
            for j in xrange(1, i):
                res[i] = map(lambda x, y:x+y, res[i-1]+[0], [0]+res[i-1])                
        return res
        
    
obj = Solution()
print obj.generate2(6)