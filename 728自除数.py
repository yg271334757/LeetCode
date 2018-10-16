class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for j in range(left, right + 1):
            if self.isDividingNumber(j):
                res.append(j)
        return res
    def isDividingNumber(self, n):
        for i in str(n):
            if i == '0':
                return False
            elif n % int(i) != 0:
                return False
        return True