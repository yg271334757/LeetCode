class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = set(s)
        if len(s) == len(l):
            return 1
        if len(l) == 1:
            return len(s)
        res = []
        tem = 0
        for i in l:
            a = s.count(i)
            if a != 1 and tem % 2 == 0:
                tem += a
            elif a != 1 and tem % 2 !=0 and a % 2 != 0:
                tem += a - 1
            elif a != 1 and tem % 2 !=0 and a % 2 == 0:
                tem += a
            res.append(a)
        if 1 in res and tem % 2 == 0:
            return tem + 1
        else:
            return tem