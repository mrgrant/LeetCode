#
# @lc app=leetcode id=275 lang=python
#
# [275] H-Index II
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(citations) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] >= len(citations) - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return len(citations) - lo
# @lc code=end

