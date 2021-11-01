#
# @lc app=leetcode id=532 lang=python
#
# [532] K-diff Pairs in an Array
#
import collections
# @lc code=start
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        d = collections.Counter(nums)
        for n in d:
            if (k > 0 and n+k in d) or (k == 0 and d[n] > 1):
                res += 1
        return res

# @lc code=end

