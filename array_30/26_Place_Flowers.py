# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:55:52 2017
#### 给定一个花坛（表示为一个包含0和1的数组，其中0表示空，1表示不为空）
#### 如果有n个新花可以种植，而不违反无邻近花的规则。(邻近花会争水源而死亡) ####
@author: Administrator
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if n <= 0:
                break;
            if (flowerbed[i]==0) and (i==0 or flowerbed[i-1]==0)  \
                and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1
                n -= 1                   
        return n <= 0
        
    def canPlaceFlowers1(self, A, N):  ## 借助 enumerate()
        for index, val in enumerate(A):
            if (not val and (index == 0 or A[index-1] == 0) 
                and (index == len(A)-1 or A[index+1] == 0)):
                N -= 1
                A[index] = 1
        return N <= 0

        
        
n = 2
flowerbed = [1,0,0,0,1,0,0,0,0,1,0] # n=1，true； n=2，false
#flowerbed = [0,0,1,0,0]
obj = Solution()
print (obj.canPlaceFlowers(flowerbed, n))
