#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#

# @lc code=start
import math
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k == len(arr):
            return arr
        dis = []
        for i, n in enumerate(arr):
            dis.append([math.fabs(n-x), i])
        dis = sorted(dis, key=(lambda x:x[0]))
        ret = []
        for i in range(k):
            ret.append(arr[dis[i][1]])
        return sorted(ret)

        
        
# @lc code=end

