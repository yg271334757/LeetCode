class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a = list(pattern)
        b = str.split()
        if len(a) != len(b):
            return False
        if len(set(a)) != len(set(b)):
            return False
        tem = dict(zip(a, b))
        for i in set(b):
            if i not in tem.values():
                return False
        return True