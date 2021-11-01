#
# @lc app=leetcode id=729 lang=python
#
# [729] My Calendar I
#
import bisect
# @lc code=start
class MyCalendar(object):

    def __init__(self):
        self.arr = [[float("-inf"), float("-inf")], [float("inf"), float("inf")]]
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        idx = bisect.bisect(self.arr, [start, end])
        if start < self.arr[idx-1][1] or end > self.arr[idx][0]:
            return False
        bisect.insort(self.arr, [start, end])
        return True

            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

