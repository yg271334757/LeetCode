class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        letters2C = dict(zip(letters, widths))
        c = 1
        l = 0
        for i in S:
            l += letters2C[i]
            if l > 100:
                c += 1
                l = letters2C[i]
        return [c, l]