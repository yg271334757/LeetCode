class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = 'aeiouAEIOU'
        s = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] in vow and s[r] in vow:
                s[l], s[r] = s[r], s[l]
                r -= 1
                l += 1
            elif s[l] in vow and s[r] not in vow:
                r -= 1
            elif s[l] not in vow and s[r] in vow:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(s)