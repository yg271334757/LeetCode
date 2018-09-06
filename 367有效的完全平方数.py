class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # [a]: 0, 1, 4, 9, 16, 25, 36, 49, 64......
        # [i]: 0, 1, 2, 3, 4,  5,  6,  7,  8 ......
        a = 0
        i = 0
        while True:
            a += i + (i + 1)
            if a == num:
                return True
            elif a > num:
                return False
            else:
                i += 1
