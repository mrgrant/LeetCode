#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        return len(intervals) - self.intervals(intervals)
    
    def intervals(self, intervals):
        intervals = sorted(intervals, key=(lambda x:x[1]))
        end = intervals[0][1]
        count = 1
        for x in intervals:
            if x[0] >= end:
                count += 1
                end = x[1]
        return count

        
# @lc code=end

