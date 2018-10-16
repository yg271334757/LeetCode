class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def isgood(x):
            dictmap = {'1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6', '0':'0'}
            a = list(str(x))
            for i, value in enumerate(a):
                if value in dictmap:
                    a[i] = dictmap[a[i]]
                else:
                    return False
            b = ''.join(a)
            if int(b) == x:
                return False
            else:
                return True
        count = 0
        for i in range(1, N+1):
            if isgood(i):
                count += 1
        return count