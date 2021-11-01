#
# @lc app=leetcode id=793 lang=python
#
# [793] Preimage Size of Factorial Zeroes Function
#

# @lc code=start
class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > 10**9:
            return 0
        return self.rightBound(k) - self.leftBound(k) + 1

        
    def trailingZeros(self, n):
        ret = 0
        divider = 5
        while n >= divider:
            ret += n // divider
            divider = divider * 5
        return ret

    def leftBound(self, k):
        lo = 0
        hi = 10**9
        while (lo < hi):
            mid = (lo + hi) // 2
            if self.trailingZeros(mid) < k:
                lo = mid + 1
            elif self.trailingZeros(mid) > k:
                hi = mid 
            else:
                hi = mid
        return lo
    
    def rightBound(self, k):
        lo = 0
        hi = 10**9

        while (lo < hi):
            mid = (lo + hi) // 2
            if self.trailingZeros(mid) < k:
                lo = mid + 1
            elif self.trailingZeros(mid) > k:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1

# @lc code=end

