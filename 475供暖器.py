class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = 0
        i = 0
        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                return max(radius, houses[-1] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))
        return radius