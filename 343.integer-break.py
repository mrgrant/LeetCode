#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        d = {1:1, 2:2, 3:3}
        for i in range(4, n+1):
            res = 1
            for k in [2, 3]:
                res = max(res, d[i-k] * d[k])
            d[i] = res
        return d[n]
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    a = obj.integerBreak(10)
