#
# @lc app=leetcode id=976 lang=python
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
import heapq
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        heap = []
        heapq.heapify(heap)
        pmax = float('inf')
        while nums:
            n = nums.pop()
            if len(heap) < 3:
                heapq.heappush(heap, -n)
            if len(heap) == 3 and -heap[0] < -(heap[1] + heap[2]):
                pmax = min(pmax, sum(heap))
            elif len(heap) == 3:
                heapq.heappop(heap)
        return 0 if pmax > 0 else -pmax



        
# @lc code=end

