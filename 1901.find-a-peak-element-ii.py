#
# @lc app=leetcode id=1901 lang=python
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            l = 0
            r = n - 1
            while l < r: 
                mid = (l+r) // 2
                if mat[i][mid] < mat[i][mid+1]:
                    l = mid + 1
                else:
                    r = mid
            if i == 0 and mat[i][l] > mat[i+1][l]:
                return [i, l]
            elif i == m - 1 and mat[i][l] > mat[i-1][l]:
                return [i, l]
            elif 0 < i < m-1 and mat[i][l] > mat[i-1][l] and mat[i][l] > mat[i+1][l]:
                return [i, l]
        return [-1, -1]
        
# @lc code=end

