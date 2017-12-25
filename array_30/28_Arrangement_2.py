# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:54:07 2017
####  Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from
 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
思路： 递归法，把最大的和最小的数去掉，剩下的情况和当初一样，做递归
##### 注意：不允许定义任何class之外的全局量，否则平台运行错误 ####
@author: Administrator
"""
import math

class Solution(object): 
    def constructArray(self, n, k):   ## 递归法在leetcode上测试有输出错误
        arr = list(range(1, n+1))
        res = []  ## 必须定义在class之内
        return self.recurse(res, arr, n, k)
        
    def recurse(self, res, arr, n, k):
        if k == 1:
            res.extend(arr)            
        elif k == 0:
            for e in arr[::-1]:  ## 倒序添加
                res.append(e)
        elif k >= 2:
            res.append(arr[0])
            res.append(arr[n-1])
            del arr[n-1], arr[0]   ## 注意删除的顺序
            return self.recurse(res, arr, n-2, k-2)        
        return res
    
    '''
        ## 大牛思路 ##
        将differ为1的元素先输出，再以此添加不为1的元素
    '''
    def constructArray1(self, n, k):  
        res = list(range(1, n - k))
        for d in range(k + 1):
            if d % 2 == 0:
                res.append(int(n - k + d/2))
            else:
                res.append(int(math.ceil(n - d/2)))
        return res

    
    
n, k = 9, 5  ## error
obj = Solution()
print (obj.constructArray1(n, k))