#
# @lc app=leetcode id=454 lang=python
#
# [454] 4Sum II
#

# @lc code=start
import collections
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                d[-(nums3[i] + nums4[j])] += 1
        res = 0
        for i in range(n):
            for j in range(n):
                if nums1[i] + nums2[j] in d:
                    res += d[nums1[i] + nums2[j]]
        return res
        
# @lc code=end

