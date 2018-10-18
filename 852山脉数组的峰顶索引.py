class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = max(A)
        for i, value in enumerate(A):
            if value == a:
                return i
        