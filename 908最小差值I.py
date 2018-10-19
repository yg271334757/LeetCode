class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        a = max(A) - min(A)
        if a <= 2 * K:
            return 0
        return a - 2*K