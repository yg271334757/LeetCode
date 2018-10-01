class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True
    def isPalindrome(self, s):
        return s == s[::-1]