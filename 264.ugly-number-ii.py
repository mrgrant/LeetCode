#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#

# @lc code=start
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for _ in range(n-1):
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
        return ugly[-1]
    
# @lc code=end

