class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # B = list(map(list, zip(*A)))
        B = []
        r = len(A)
        c = len(A[0])
        for _ in range(c):
            B.append([0] * r)
        for i in range(c):
            for j in range(r):
                B[i][j] = A[j][i]
        return B