class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c**0.5)+1):
            if ((c-i*i)**0.5).is_integer(): 
                return True
        return False