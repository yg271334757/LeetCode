class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        a = bin(N)[2:]
        if a.count('1') < 2:
            return 0
        length = 1
        maxv = 0
        for i in a:
            if i == '1':
                maxv = max(length, maxv)
                length = 1
            else:
                length += 1
        return maxv