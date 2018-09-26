class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        m = int(len(s) // k)
        s = list(s)
        for i in range(m + 1):
            if i % 2 == 0:
                s[i * k : (i + 1) * k] = reversed(s[i * k : (i + 1) * k])
        return ''.join(s)