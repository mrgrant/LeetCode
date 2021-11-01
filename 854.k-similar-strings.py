#
# @lc app=leetcode id=854 lang=python
#
# [854] K-Similar Strings
#

# @lc code=start
class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        level = 0
        visit = set()
        q = [s1]
        while q:
            temp = []
            for node in q:
                if node == s2:
                    return level
                neighbor = self.getNeighbor(node, s2)
                for nbrNode in neighbor:
                    if nbrNode in visit:
                        continue
                    visit.add(nbrNode)
                    temp.append(nbrNode)
            q = temp
            level += 1
        return -1



    def getNeighbor(self, s1, s2):
        sList = list(s1)
        i = 0
        neighbor = []
        while s1[i] == s2[i]:
            i += 1
        for j in range(i+1, len(s2)):
            if s2[j] == s1[i]:
                sList[i], sList[j] = sList[j], sList[i]
                neighbor.append("".join(sList))
                sList[i], sList[j] = sList[j], sList[i]
        return neighbor

# @lc code=end

