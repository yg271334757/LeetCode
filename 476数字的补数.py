class Solution:
    def findComplement(self,num):
        """
        :type num: int
        :rtype: int
        """
        a = bin(num)[2:]
        b = [0] * len(a)
        for i in range(len(a)):
            if a[i] == '1':
                b[i] = '0'
            elif a[i] == '0':
                b[i] = '1'
        tem = ''.join(b)
        return int(tem,2)
        