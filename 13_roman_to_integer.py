class Solution:
    def romanToInt(self, s):
        p ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if s == '0':
            return 0
        else:
            res = 0
            for i in range (0,len(s)):
                if i == 0 or p[s[i]] <= p[s[i-1]]:
                    res += p[s[i]]
                else:
                    res += p[s[i]] - 2 * p[s[i-1]]
            return res