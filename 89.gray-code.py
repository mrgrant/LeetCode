#
# @lc app=leetcode id=89 lang=python
#
# [89] Gray Code
#

# @lc code=start
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(0, n):
            size = len(ret)
            for j in range(0, size)[::-1]:
                ret.append(ret[j] | 1<<i)
        return ret
        
# @lc code=end

