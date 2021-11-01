#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: 
            return 0
        if n == 1:
            return 1
        f0 = 0
        f1 = 1
        for i in range(1, n):
            f0, f1 = f1, f0 + f1
        return f1
# @lc code=end

