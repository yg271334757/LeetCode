# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:53:34 2018

@author: Gang Yang
"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.a.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.a.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.a[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.a) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
