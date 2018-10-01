class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 1
        while i < len(B) // len(A) + 3:
            C = A * i
            if len(C) > len(B) + len(A):
                if B in C:
                    return i
                else:
                    return -1
            elif B in C:
                return i
            elif len(C) == len(B):
                if B in C:
                    return i
            i += 1