class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        for i in s:
            if i not in res:
                if s.count(i) == 1:
                    return s.index(i)
                else:
                    res.append(i)
        return -1