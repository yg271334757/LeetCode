class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # return bin(x ^ y).count('1')
        ax = ['0'] * 31
        by = ['0'] * 31
        a = bin(x)[2:]
        b = bin(y)[2:]
        for i in range(len(a)):
            ax[30 - i] = a[len(a) - i - 1]
        for j in range(len(b)):
            by[30 - j] = b[len(b) - j - 1]
        count = 0
        for k in range(len(ax)):
            if ax[k] != by[k]:
                count += 1
        return count