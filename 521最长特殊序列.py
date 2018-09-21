class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) > len(b):
            return len(a)
        elif len(b) > len(a):
            return len(b)
        else:
            if a == b:
                return -1
            else:
                return len(a)