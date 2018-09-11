class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = n // 2
        while (i* (i + 1)) / 2 <= n:
            i += 1
        return i