class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        S = (A + ' ' + B).split()
        res = []
        for i in set(S):
            if S.count(i) == 1:
                res.append(i)
        return res