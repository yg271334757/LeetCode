class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        tem = ''.join(reversed(S))
        a = tem.split('-')
        tem1 = ''.join(a)
        j = 0
        res = ''
        while True:
            if j == len(tem1):
                break
            res += tem1[j].upper()
            if (j + 1) % K == 0 and j != len(tem1) - 1:
                res += '-'
            j += 1
        return res[::-1]