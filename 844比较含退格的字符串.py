class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def clear(x):
            ans = []
            for i in x:
                if i != '#':
                    ans.append(i)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        return clear(S) == clear(T)