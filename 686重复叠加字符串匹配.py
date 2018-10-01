class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = len(B) // len(A)
        while i < len(B) // len(A) + 3:
            if B in A * i:
                return i
            i += 1
        return -1