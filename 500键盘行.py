class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        res=[]
        for i in words:
            for j in range(len(i)):
                a = i[j].lower()
                if i[0].lower() in row1 and a not in row1:   
                    break
                if i[0].lower() in row2 and a not in row2:
                    break
                if i[0].lower() in row3 and a not in row3:
                    break
                if j == len(i) - 1:
                    res.append(i)
        return res