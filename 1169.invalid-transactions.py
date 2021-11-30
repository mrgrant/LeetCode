#
# @lc app=leetcode id=1169 lang=python
#
# [1169] Invalid Transactions
#

# @lc code=start
import collections
class Trans:
    def __init__(self, name, time, money, city, command):
        self.name = name
        self.time = time
        self.money = money 
        self.city = city
        self.command = command

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        transList = []
        for command in transactions:
            cmd = command.split(",")
            trans = Trans(cmd[0], int(cmd[1]), int(cmd[2]), cmd[3], command)
            transList.append(trans)
        transList = sorted(transList, key = lambda x: x.time)
        res = []
        d = collections.defaultdict(list)

        for tran in transList:
            while len(d[tran.name]) > 0 and tran.time - d[tran.name][0].time > 60:
                t = d[tran.name].pop(0)
                if t.money > 1000:
                    res.append(t.command)

            if len(d[tran.name]) > 0 and tran.time - d[tran.name][-1].time < 60 and tran.city != d[tran.name][-1].city:
                d[tran.name].append(tran)
                for ttran in d[tran.name]:
                    res.append(ttran.command)
                d[tran.name] = []
            else:
                d[tran.name].append(tran)
            
        for key in d:
            for tran in d[key]:
                if tran.money > 1000:
                    res.append(tran.command)
        
        return res
        
# @lc code=end
if __name__ == "__main__":
    obj = Solution()
    transactions = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
    a = obj.invalidTransactions(transactions)
