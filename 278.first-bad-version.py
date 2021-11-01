#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        mid = lo + (hi - lo) // 2
        while lo < hi:
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
            mid = lo + (hi - lo) // 2
        return lo
# @lc code=end

