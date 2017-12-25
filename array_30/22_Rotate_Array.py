# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:16:03 2017

@author: Administrator
Description：Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] 
is rotated to [5,6,7,1,2,3,4].
"""
class Solution(object):
    def rotate(self, nums, k):  #k值可以无限循环的
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k] ##一定要在原位置进行修改，必须＋ [:]
        return nums
    
    def rotate1(self, nums, k): ## 
        N = len(nums) - 1
        for i in xrange(N, N - k, -1):
            nums.insert(0, nums[N])
            del nums[N+1]
        return nums



nums = [1,2,3,4,5,6,7] 
obj = Solution()
print (obj.rotate(nums, 3))

'''List操作:
## list[:] = b, 表示在原list上做修改
## list = a + b，只是普通的连接操作，只是创建了一个list的副本
## 在原位置上修改可以用extend()
'''