# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:36:56 2017

@author: Administrator
"""
''' Description
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
'''   

class Solution(object):
    def matrixReshape(self, nums, r, c):
        if len(nums)*len(nums[0]) != r*c:
            return nums
        vals = [val for row in nums for val in row]
        ans = [[None]*c for _ in xrange(r)]
        i = 0;
        for rr in xrange(r):
            for cc in xrange(c):
                ans[rr][cc] = vals[i]
                i += 1
        return ans


arr = [[1,3],[2,4],[6,7]]
obj = Solution()
res = obj.matrixReshape(arr, 2, 3)

'''
class Solution(object):
    def matrixReshape(self, nums, r, c):   
        if len(nums)*len(nums[0]) != r*c:
            return nums
        vals = (val for row in nums for val in row)
        return [[vals.next() for c in xrange(c)] for r in xrange(r)]
'''