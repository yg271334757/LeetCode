class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        a = bin(num)[2:]
        if a.count('1') == 1:
            if len(a) % 2 == 0:
                return False
            else:
                return True
        else:
            return False
        """
        if num < 1:
                return False
            while num % 4 == 0:
                num >>= 2
            return num == 1
        """