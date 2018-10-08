class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split(' ')))
        return sum(min(a,b) for a,b in zip(L, L[1:]))