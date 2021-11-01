#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = collections.defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            if c not in d or d[c] <= 0:
                return False
            d[c] -= 1
        return True
        
# @lc code=end

