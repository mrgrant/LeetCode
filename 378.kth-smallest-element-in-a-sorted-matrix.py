#
# @lc app=leetcode id=378 lang=python
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m_extend = []
        for l in matrix:
            m_extend.extend(l)
        m_extend = sorted(m_extend)
        return m_extend[k-1]
        
# @lc code=end

