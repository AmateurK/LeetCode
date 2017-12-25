# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 10:57:12 2017

@author: Administrator
"""
''' Description ###计算灰度
Given a 2D integer matrix M representing the gray scale of an image, you need 
to design a smoother to make the gray scale of each cell becomes the average gray scale
 (rounding down) of all the 8 surrounding cells and itself. 
 If a cell has less than 8 surrounding cells, then use as many as you can.
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
'''

class Solution(object): #直接找8-邻接元素
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        xlen = len(M)
        ylen = len(M[0]) if xlen else 0
        res = [[0 for i in xrange(len(M[0]))] for j in xrange(len(M))]
        for x in xrange(xlen):
            for y in xrange(ylen):
                neibo = [
                        M[a][b] 
                        for a in (x-1, x, x+1)
                        for b in (y-1, y, y+1)
                        if 0 <= a < xlen and 0 <= b < ylen
                        ]
                res[x][y] = sum(neibo) // len(neibo)
        return res

class Solution1(object):  #定义模板算子矩阵
    def imageSmoother(self, M):
        if not M: return M
        direction = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1))
        res = [[0 for i in xrange(len(M[0]))] for j in xrange(len(M))]
        
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                tot = 0
                cnt = 0                
                for r,c in direction:
                    if i+r<0 or i+r>=len(M) or j+c<0 or j+c>=len(M[0]):
                        continue
                    tot += M[i+r][j+c]
                    cnt += 1
                res[i][j] = tot / cnt
        return res

class Solution2(object):  #在外围增加一圈元素
    def imageSmoother(self, M):
        res = [[0 for i in xrange(len(M[0]))] for j in xrange(len(M))]
        M.insert(0,[-1 for i in xrange(len(M[0]))])
        M.append([-1 for i in xrange(len(M[0]))])
        for i in xrange(len(M)):
            M[i].append(-1)
            M[i].insert(0,-1)
        ## Insert End
        for i in xrange(1, len(M)-1):
            for j in xrange(1, len(M[0])-1): 
                tot = 0
                cnt = 0                
                for r in xrange(-1, 2): # 不包括2
                    for c in xrange(-1, 2):
                        if M[i+r][j+c] != -1:
                            tot += M[i+r][j+c]
                            cnt += 1
                res[i-1][j-1] = tot / cnt
        return res
                
                
nums = [[4,2,3,0],[5,0,6,1],[1,0,1,4],[0,2,1,1]]
obj = Solution()
print obj.imageSmoother(nums)


''' MY (Error)
import numpy as np
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [[0 for i in xrange(len(M))] for i in xrange(len(M))]
        L1 = len(M) - 1
        L2 = len(M) - 2
        L3 = len(M) - 2
        
        ans[0][0] = int(np.floor((M[0][0]+M[0][1]+M[1][0]+M[1][1])/4))
        ans[0][L1] = int(np.floor((M[0][L1]+M[0][L2]+ M[1][L1]+M[1][L2])/4))
        ans[L1][0] = int(np.floor((M[L1][0]+M[L2][0]+ M[L1][1]+M[L2][1])/4))
        ans[L1][L1] = int(np.floor((M[L1][L1]+M[L2][L1]+ M[L1][L2]+M[L2][L2])/4))
        
        for i in xrange(L2):
            ans[0][i+1] = int(np.floor((M[0][i]+M[0][i+1]+M[0][i+2]+ \
               M[1][i]+M[1][i+1]+M[1][i+2])/6))
        for i in xrange(L2):
            ans[L1][i+1] = int(np.floor((M[L1][i]+M[L1][i+1]+M[L1][i+2]+ \
               M[L2][i]+M[L2][i+1]+M[L2][i+2])/6))
        for i in xrange(L2):
            ans[i+1][0] = int(np.floor((M[i][0]+M[i+1][0]+M[i+2][0]+ \
               M[i][1]+M[i+1][1]+M[i+2][1])/6))
        for i in xrange(L2):
            ans[i+1][L1] = int(np.floor((M[i][L1]+M[i+1][L1]+M[i+2][L1]+ \
               M[i][L2]+M[i+1][L2]+M[i+2][L2])/6))
            
        for i in xrange(L3):
            for j in xrange(L3):
                ans[i+1][j+1] = int(np.floor((M[i][j]+M[i][j+1]+M[i][j+2]+ \
                   M[i+1][j]+M[i+1][j+1]+M[i+1][j+2]+ M[i+2][j]+M[i+2][j+1]+M[i+2][j+2]) / 9))
                        
        return ans
'''