# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while l + 1< r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            if not isBadVersion(mid):
                l = mid
        return r