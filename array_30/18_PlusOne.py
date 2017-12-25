# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:46:45 2017

@author: Administrator
"""
''' Description
Given a non-negative integer represented as a non-empty array of digits, 
plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
digits = [9], digits = [2,3,9,9]
'''
class Solution(object):
    def plusOne(self, digits): ### Idea: array->int->array
        """
        :type digits: List[int]
        :rtype: List[int]
        """    
        strnum = ''
        for i in xrange(len(digits)):
            strnum += str(digits[i])
        dd = int(strnum)
        dd += 1
        nums = []        
        while dd != 0:
            rest = dd % 10
            dd /= 10
            nums.insert(0, rest)
        return nums
    
    def plusOne1(self, digits): ### 简化上面代码
        """
        :type digits: List[int]
        :rtype: List[int]
        """    
        strnum = ''
        for i in range(len(digits)):
            strnum += str(digits[i])
        return [int(x) for x in str(int(strnum) + 1)]
    
    
    def plusOne2(self, digits):  ##数组转换成数字
        num = 0
        for i in range(len(digits)):
        	num += digits[i] * pow(10, (len(digits)-1-i)) 
        return [int(i) for i in str(num+1)]
            
        
digits = [2,9,9,9]
obj = Solution()
print (obj.plusOne1(digits))