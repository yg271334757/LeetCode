class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = list(reversed(A[i]))
            for j in range(len(A[i])):
                # A[i][j] = 1 ^ A[i][j]
                A[i][j] = 1 - A[i][j] # This is much faster
        return A