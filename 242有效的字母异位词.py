class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        stack = ''
        for i in s:
            if i in stack:
                continue
            else:
                stack += i
            if s.count(i) != t.count(i):
                return False
        return True