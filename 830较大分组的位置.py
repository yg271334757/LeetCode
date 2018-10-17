class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        l = 0
        r = 1
        res = []
        while r < len(S):
            if S[l] != S[r]:
                if r - l >= 3:
                    res.append([l, r - 1])
                l = r
            r += 1
        if r - l >= 3:
            res.append([l, r-1])
        return res