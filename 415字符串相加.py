class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        numsMap = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5':5, '6': 6, '7': 7, '8': 8, '9': 9}
        a = 0
        b = 0
        for i in range(len(num1)):
            a += numsMap[num1[i]] * 10 ** i
        for j in range(len(num2)):
            b += numsMap[num2[j]] * 10 ** j
        return '{}'.format(a + b)