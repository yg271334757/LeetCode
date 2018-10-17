class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexC = []
        for i, value in enumerate(S):
            if value == C:
                indexC.append(i)
        indexC.append(float('inf'))
        res = []
        m = 0
        for j in range(len(indexC) - 1):
            for k in range(m, len(S)):
                a = abs(k - indexC[j])
                b = abs(k - indexC[j + 1])
                if a <= b:
                    res.append(a)
                else:
                    res.append(b)
                    m = k + 1
                    break
        return res
                