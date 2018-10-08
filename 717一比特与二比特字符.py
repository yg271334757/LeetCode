class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        encode = 0
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                encode = 1
                i += 2
            else:
                encode = 0
                i += 1
        return encode