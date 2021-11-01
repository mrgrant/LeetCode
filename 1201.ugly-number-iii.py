#
# @lc app=leetcode id=1201 lang=python
#
# [1201] Ugly Number III
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        u = 0
        ia, ib, ic = 1, 1, 1
        for _ in range(n):
            ua, ub, uc = a*ia, b*ib, c*ic
            umin = min(ua, ub, uc)
            if umin == ua:
                ia += 1
            if umin == ub:
                ib += 1
            if umin == uc:
                ic += 1
            u = umin
        return u
        
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    a = obj.nthUglyNumber(5, 2, 11, 13)
