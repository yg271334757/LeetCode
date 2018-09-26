class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        elif 'LLL' in s:
            return False
        else:
            return True