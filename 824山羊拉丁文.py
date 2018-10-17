class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        for i in range(len(words)):
            if words[i][0] in ['a','e','i','o','u','A','E','I','O','U']:
                words[i] += 'ma'
            elif words[i][0] not in ['a','e','i','o','u','A','E','I','O','U']:
                words[i] = words[i][1: ] + words[i][0] + 'ma'
            words[i] = words[i] + ('a' * (i + 1))
        return ' '.join(words)