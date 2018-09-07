import itertools
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        time = []
        for k in range(num + 1):
            time_hour = self.choice_hour( k)
            time_minute = self.choice_minute(num - k)
            for n in time_hour:
                for m in time_minute:
                    if m < 10:
                        time.append('{0}:0{1}'.format(n, m))
                    else:
                        time.append('{0}:{1}'.format(n, m))
        return time

    def choice_hour(self, x):
        if x == 0:
            return [0]
        hours = [1, 2, 4, 8]
        res = []
        for a in itertools.combinations(hours, x):
            if sum(a) not in res and sum(a) < 12:
                res.append(sum(a))
        return res
    
    def choice_minute(self, x):
        if x == 0:
            return [0]
        minutes = [1, 2, 4, 8, 16, 32]
        res = []
        for a in itertools.combinations(minutes, x):
            if sum(a) not in res and sum(a) < 60:
                res.append(sum(a))
        return res