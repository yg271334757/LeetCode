class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tem = len(bin(n))
        res = 0
        if n % 2 == 0:
            for i in range(tem - 2):
                if i % 2 != 0:
                    res += 2 ** i
        elif n % 2 != 0:
            for i in range(tem - 2):
                if i % 2 == 0:
                    res += 2 ** i
        return res == n