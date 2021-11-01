#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        ret = []
        def backtrack(s, start, str):
            if start == len(s):
                ret.append(" ".join(str))
                return 
            for i in range(start, len(s)+1):
                if s[start:i] in wordDict:
                    str.append(s[start:i])
                    backtrack(s, i, str)
                    str.pop()
                else:
                    continue
        backtrack(s, 0, [])
        return ret
# @lc code=end

if __name__ == "__main__":
    obj = Solution()
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    a = obj.wordBreak(s, wordDict)
