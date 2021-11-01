#
# @lc app=leetcode id=475 lang=python
#
# [475] Heaters
#

# @lc code=start
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters)
        def bin_search(array, target):
            # return max index larger or equal than target
            lo = 0
            hi = len(array)
            while lo < hi:
                mid = (lo + hi) // 2
                if array[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid     
            return lo
        
        res = 0
        lh = len(heaters)
        for h in houses:
            left_bound = bin_search(heaters, h)
            if left_bound >= lh:
                res = max(res, abs(h - heaters[-1]))
            elif left_bound > 0 and left_bound < lh:
                res = max(res, min(abs(heaters[left_bound] - h), abs(heaters[left_bound-1] - h)))
            elif left_bound == 0:
                res = max(res, abs(h - heaters[left_bound])   )
        return res
# @lc code=end

