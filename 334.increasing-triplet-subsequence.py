#
# @lc app=leetcode id=334 lang=python
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
# @lc code=end

