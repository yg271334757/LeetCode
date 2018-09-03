class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [0] * 100
        dp[0] = num
        #dp[1] = nums // 10 + nums % 10
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] // 10 + dp[i - 1] % 10
            if len(str(dp[i])) == 1:
                return dp[i]