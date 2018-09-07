class Solution:
    # O(n)space cost
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
    
    # O(1) space cost
    '''
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count
    '''    