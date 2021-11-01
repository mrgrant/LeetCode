#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n <= 1:
            ret += (n // 5)
            n = n // 5
        return ret
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    obj.trailingZeroes(5)
