class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = 0
        f2 = 0
        for i in reversed(cost):
            f1, f2 = i + min(f1, f2), f1
        return min(f1, f2)