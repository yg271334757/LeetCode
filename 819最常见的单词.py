import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        letters = re.findall('[a-z]+', paragraph)
        count = {}
        for letter in letters:
            if letter not in banned and letter not in count:
                count[letter] = 1
            elif letter not in banned and letter in count:
                count[letter] += 1
        return max(count.items(), key=lambda x: x[1])[0]