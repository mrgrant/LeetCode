#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
#

# @lc code=start
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict(int)
        for c in list(s):
            d[c] += 1
        li = []
        for key in d:
            li.append([-d[key], key])
        li = sorted(li, key = lambda x: x[0])
        res = ""
        for freq, c in li:
            res += c * (-freq)
        return res
# @lc code=end

