class Solution:
     def letterCasePermutation(self, S):
            """
            :type S: str
            :rtype: List[str]
            """
            res = [S]
            for i, c in enumerate(S):
                if c.isalpha():
                    res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
            return res