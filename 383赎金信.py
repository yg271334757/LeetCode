class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine.remove(i)
        return True