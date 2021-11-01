#
# @lc app=leetcode id=1326 lang=python
#
# [1326] Minimum Number of Taps to Open to Water a Garden
#

# @lc code=start
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        max_range= [0 for _ in range(len(ranges))]
        for i in range(len(ranges)):
            left = max(i - ranges[i], 0)
            right = min(i + ranges[i], n)
            max_range[left] = max(max_range[left], right )
        start = end = step = 0
        while end < n:
            step += 1
            start, end = end, max(max_range[i] for i in range(start, end+1))
            if start == end:
                return -1
        return step

        
# @lc code=end

