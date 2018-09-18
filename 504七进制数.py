class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        ans = ''
        a = abs(num)
        while a != 0:
            ans += str(abs(a % 7))
            a = abs(a) // 7
        if num >= 0:
            return ans[::-1]
        else:
            return '-' + ans[::-1]