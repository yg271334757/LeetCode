class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(set(A)) != len(A) and A == B:
            return True
        tem = []
        for i in range(len(A)):
            if A[i] != B[i]:
                tem.append([A[i], B[i]])
        if len(tem) == 2 and tem[0] == tem[1][::-1]:
            return True
        return False