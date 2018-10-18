class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        stack = {5:1, 10:0}
        for i in bills[1:]:
            if i == 5:
                stack[5] += 1
            elif i == 10:
                if stack[5] == 0:
                    return False
                stack[5] -= 1
                stack[10] += 1
            elif i == 20:
                if stack[5] >= 1 and stack[10] >= 1:
                    stack[5] -= 1
                    stack[10] -= 1
                elif stack[5] >= 3 and stack[10] == 0:
                    stack[5] -= 3
                else:
                    return False
        return True