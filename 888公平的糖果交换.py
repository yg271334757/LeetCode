class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        x = (sum(A) - sum(B)) // 2
        B = set(B)
        for a in A:
            if a - x in B:
                return [a, a-x]