class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        tem = []
        nol = {}
        for i, v in enumerate(S):
            if v.isalpha():
                tem.append(v)
            else:
                nol[i] = v
        tem = tem[::-1]
        order = sorted(nol.keys())
        for k in order:
            tem.insert(k, nol[k])
        return ''.join(tem)