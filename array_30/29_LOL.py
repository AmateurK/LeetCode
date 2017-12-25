# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:35:42 2017
##### LOL中的英雄攻击问题  ####
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.
@author: Administrator
"""
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        dura = 0
        for i in range(1, len(timeSeries)): # if--else可以柔和成max()
            dura += duration - max(0, timeSeries[i-1] + duration - timeSeries[i])
        return 0 if len(timeSeries)==0 else dura + duration
    
    
    def findPoisonedDuration1(self, timeSeries, duration): #[2,2,2]
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans



timeSeries = [1, 4, 5,8,9,10] 
#timeSeries = [] 
duration = 2
obj = Solution()
print (obj.findPoisonedDuration(timeSeries, duration))