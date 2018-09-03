class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        #stack = ''
        for i in set(s):
            #if i not in stack:
                #stack += i
            #else:
                #continue
            if s.count(i) != t.count(i): 
               return False
        return True
