#
# @lc app=leetcode id=697 lang=python
#
# [697] Degree of an Array
#

# @lc code=start
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        start = {}
        end = collections.defaultdict(int)
        _max = 0
        res = float("inf")
        for i, n in enumerate(nums):
            if n not in start:
                start[n] = i
            cnt[n] += 1
            end[n] = i
            if cnt[n] > _max:
                _max = max(_max, cnt[n])
        for n in cnt:
            if cnt[n] == _max:
                res = min(res, end[n] - start[n] + 1)
        return res
                
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    a = obj.findShortestSubArray([1, 2, 2, 3, 1])

