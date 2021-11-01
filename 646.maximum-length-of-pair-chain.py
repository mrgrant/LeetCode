#
# @lc app=leetcode id=646 lang=python
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key = lambda x: x[1])
        res = 1
        cur = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > cur:
                res += 1
                cur = pairs[i][1]
        return res

        

# @lc code=end

