#
# @lc app=leetcode id=372 lang=python
#
# [372] Super Pow
#

# @lc code=start
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a % 1337 == 0:
            return 0
        else:
            exponent = int( ''.join( map( str, b) ) )
            return pow(a,exponent % 1140,1337)
# @lc code=end
