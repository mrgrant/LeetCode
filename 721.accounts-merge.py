#
# @lc app=leetcode id=721 lang=python
#
# [721] Accounts Merge
#

# @lc code=start
import collections
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        visit = [False for _ in range(len(accounts))]
        d = collections.defaultdict(list)
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                d[email].append(i)
        
        def dfs(n, emails):
            if visit[n]:
                return 
            visit[n] = True
            for e in accounts[n][1:]:
                emails.add(e)
                for accnum in d[e]:
                    dfs(accnum, emails)
        
        res = []
        for i, account in enumerate(accounts):
            if visit[i] == True:
                continue
            emails = set()
            dfs(i, emails)
            res.append([account[0]] + sorted(list(emails)))
        return res

        
# @lc code=end

