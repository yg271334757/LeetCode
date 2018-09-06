class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            a = list(s)
            b = list(t)
        elif len(s) > len(t):
            a = list(t)
            b = list(s)
        a.sort()
        b.sort()
        l = a + b[::-1]
        i = 0
        j = len(l) - 1
        while i <= j:
            if l[i] == l[j]:
                i += 1
                j -= 1
            else:
                return l[j]
        return l[j + 1]