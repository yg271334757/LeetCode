# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:57:31 2018

@author: Gang Yang
"""
import itertools
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            tem = []
            for key, group in itertools.groupby(self.countAndSay(n - 1)):
                tem.append(list(group))
            res = []
            for i in range(len(tem)):
                times = tem[i].count(tem[i][0])
                res.append('{0}{1}'.format(times,tem[i][0]))
                a = ''.join(res)
            return str(a)