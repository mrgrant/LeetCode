#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = str(bin(n))[2:]
        while len(b) < 32:
            b = "0" + b
        return int(b[::-1], 2)
        
# @lc code=end

