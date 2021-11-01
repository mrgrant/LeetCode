#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def getHour(piles, speed):
            res = 0
            for pile in piles:
                res += math.ceil(pile / speed)
            print(res, speed)
            return res
        lo = 1 
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if getHour(piles, mid) >= h:
                lo = mid + 1
            else:
                hi = mid
        return lo

if __name__ == "__main__":
    obj = Solution()
    a = obj.minEatingSpeed([30,11,23,4,20], 5)
        
# @lc code=end

