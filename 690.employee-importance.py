#
# @lc app=leetcode id=690 lang=python
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        res = 0
        d = {}
        for e in employees:
            d[e.id] = e
        stack = [id]
        while stack:
            temp = []
            for idx in stack:
                res += d[idx].importance 
                temp.extend(d[idx].subordinates)
            stack = temp
        return res
# @lc code=end

