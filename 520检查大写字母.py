class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1:].isupper():
                return True
            elif word[1:].islower():
                return True
            else:
                return False
        elif word[0].islower():
            return word[1:].islower()