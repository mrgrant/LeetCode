#
# @lc app=leetcode id=525 lang=python
#
# [525] Contiguous Array
#

# @lc code=start
import collections
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smax = 0
        count = 0
        d = {}
        d[0] = 0
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1
            if count not in d:
                d[count] = i + 1
            else:
                smax = max(smax, i + 1 - d[count])
        return smax
        
# @lc code=end

