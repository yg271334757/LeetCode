class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordList = s.split()
        reversedWordList = []
        for i in wordList:
            reversedWordList.append(i[: : -1])
        return ' '.join(reversedWordList)