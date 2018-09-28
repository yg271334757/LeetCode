class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        origin = [0, 0]
        if len(moves) % 2 != 0:
            return False
        for i in moves:
            if i == 'R':
                origin[0] += 1
            elif i == 'L':
                origin[0] -= 1
            elif i == 'U':
                origin[1] += 1
            elif i == 'D':
                origin[1] -= 1
        if origin == [0, 0]:
            return True
        else:
            return False