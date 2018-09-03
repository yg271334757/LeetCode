class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        dp = [0] * 100
        dp[0] = num
        for i in range(1,len(dp)):
            for j in [2, 3, 5]:
                if dp[i - 1] % j == 0:
                    dp[i] = dp[i - 1] / j
            if dp[i] == 1:
                return True
            if dp[i] == 0:
                return False