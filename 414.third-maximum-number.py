#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = None
        max2 = None
        max3 = None
        for n in nums:
            if n == max1 or n == max2 or n == max3:
                continue
            if max1 is None or n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif max2 is None or max2 < n < max1:
                max3 = max2
                max2 = n
            elif max3 is None or max3 < n < max2:
                max3 = n
        return max1 if max3 is None else max3
                

# @lc code=end

