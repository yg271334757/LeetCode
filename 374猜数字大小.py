# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right,mid = 1, n, 0
        while left <= right:
            mid = (left+right)/2
            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                left=mid+1
            else:
                right=mid-1
        return mid