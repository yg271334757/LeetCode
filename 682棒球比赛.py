class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if i == 'C':
                stack.pop()
            elif i == '+':
                stack.append(stack[-2] + stack[-1])
            elif i == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)