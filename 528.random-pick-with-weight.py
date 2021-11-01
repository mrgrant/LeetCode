#
# @lc app=leetcode id=528 lang=python
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        s = sum(w)
        for i in range(1, len(w)):
            w[i] = w[i] + w[i-1]
        self.rate = [val*1.0/s for val in w]

    
    def bin_search(self, target):
        lo = 0
        hi = len(self.rate)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.rate[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
        

    def pickIndex(self):
        """
        :rtype: int
        """
        return self.bin_search(random.random())
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

