#
# @lc app=leetcode id=220 lang=python
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def getIdx(n, w):
            if n >= 0:
                return n // w
            else:
                return n // w - 1
        
        buckets = {}
        w = t + 1
        for i in range(len(nums)):
            n = nums[i]
            bucketId = getIdx(n, w)
            if bucketId in buckets:
                return True
            elif (bucketId-1) in buckets and n - t <= buckets[bucketId-1] <= n + t:
                return True
            elif (bucketId+1) in buckets and n - t <= buckets[bucketId+1] <= n + t:
                return True
            buckets[bucketId] = n
            if i >= k:
                del buckets[getIdx(nums[i-k], w)]
        return False
            

    
# @lc code=end

